import os
import time
import argparse
import threading
import json

import numpy as np

import torch
import torch.distributed as dist
from torch.utils.data import DataLoader

from aperturedb import Connector, ConnectorRest
from aperturedb import PyTorchDataset

from infer import BboxDetector as BboxDetector

MAX_RETRIEVED = 1000
SCALE = 0.5
SAVE_TO_FILE = False
query_file = open("queries.json", "w")

stop = False

import logging
logging.basicConfig(
    level=os.environ.get('LOG_CONSOLE_LEVEL', 'ERROR').upper()
)

def log_info(db, msg, level="INFO"):
    """
    Log to both console and aperturedb (for Grafana annotations)
    """
    print(msg, flush=True)
    query = [dict(UserLogMessage=dict(type=level, text="find_clip: " + msg))]
    status, _ = db.query(query)
    print(query, status, flush=True)
    assert 0 == status[0]['UserLogMessage']['status'], str((query, status))

def push_to_aperturedb(db, img_id, detections, classes, source):

    q = [{
        "FindImage": {
            "_ref": 1,
            "blobs": False,
            "constraints": {
                "_uniqueid": ["==", img_id]
            },
        }
    }]

    for box, score, label in zip(detections["boxes"], detections["scores"], detections["labels"]):

        if float(score) < 0.5:
            continue

        box = box.detach().cpu().numpy()
        idx = int(label)
        label = classes[idx]

        abb = {
            "AddBoundingBox": {
                "image_ref": 1,
                "label": label,
                "rectangle": {
                    "x": int(box[0] / SCALE),
                    "y": int(box[1] / SCALE),
                    "width":  int((box[2] - box[0]) / SCALE),
                    "height": int((box[3] - box[1]) / SCALE)
                },
                "properties": {
                    "source": source,
                    "confidence": float(score),
                },
            }
        }

        # print(abb)

        q.append(abb)

    # print(q)

    if SAVE_TO_FILE:
        query_file.write(json.dumps(q))
        query_file.write("\n")
    else:
        db.query(q)

        if not db.last_query_ok():
            db.print_last_response()
        # else:
        #     print("query ok")

def cleanup_bboxes_from_aperturedb(db, source):

    q = [{
        "DeleteBoundingBox": {
            "constraints": {
                "source": ["==", source]
            }
        }
    }]

    print(f"Cleaning up bboxes with source: {source} from ApertureDB...")

    db.query(q)

    if not db.last_query_ok():
        db.print_last_response()

    print(f"Done cleaning up.")

def push_to_aperturedb_queue(db_obj, queue, classes, model_name):

    print("Starting thread", flush=True)

    db = db_obj.create_new_connection()

    counter = 0
    while True:
        if stop:
            print("Thread stopping.")
            return

        if len(queue) == 0:
            counter += 1

            if counter > 10:
                print("Thread returning after 5 secs.")
                return

            time.sleep(1)
            continue
            # if len(queue) == 0:
            #     print("Thread returning after 5 secs.")
            #     return

        img_id, detections = queue.pop()
        push_to_aperturedb(db, img_id, detections, classes, model_name)

        counter = 0

def main(params):

    print(f"Connecting to ApertureDB...")

    db = Connector.Connector(host="coco-jxdx0bzi.farm0003.cloud.aperturedata.io",
                             user="admin", password="V@tsal0710")

    if params.clean:
        cleanup_bboxes_from_aperturedb(db, params.model_name)

    q = [{
        "FindImage": {
            "constraints": {
                "license": [">=", 0]
            },
            "limit": MAX_RETRIEVED,
            "operations": [
                {
                    "type": "resize",
                    "scale": 0.5
                }
            ],
            "results": {
                "list": ["_uniqueid"]
            }
        }
    }]

    print(f"Creating dataset...")
    dataset = PyTorchDataset.ApertureDBDataset(db, q, batch_size=1, label_prop="_uniqueid")

    total = len(dataset)
    print("Total images in the dataset:", total)

    batch_size = 1

    # === Distributed Data Loader Sequential
    print("Distributed Data Loader Sequential")
    data_loader = DataLoader(
        dataset,
        batch_size=batch_size,          # pick random values here to test
        num_workers=8,          # num_workers > 1 to test multiprocessing works
        pin_memory=True,
        drop_last=True,
        prefetch_factor=4
    )


    # === Distributed Data Loader Shuffler
    # This will generate a random sampler, which will make the use
    # of batching wasteful
    sampler = torch.utils.data.DistributedSampler(dataset, shuffle=True)

    data_loader_shuffle = DataLoader(
        dataset,
        sampler=sampler,
        batch_size=batch_size,  # pick random values here to test
        num_workers=8,          # num_workers > 1 to test multiprocessing works
        pin_memory=True,
        drop_last=True,
        prefetch_factor=4,
    )

    detector = BboxDetector(model_name=params.model_name)

    # # Retrieve all the images
    log_info(db, f"From DataLoaders Sequential. n={MAX_RETRIEVED}")

    queue = [] # detection queue

    thds = []
    for i in range(1):
        x = threading.Thread(target=push_to_aperturedb_queue,
                            args=(db, queue, detector.classes, params.model_name))
        x.start()
        thds.append(x)

    start = time.time()
    imgs = 0

    for img, img_id in data_loader:
        start_infer = time.time()
        detections = detector.infer(np.array(img[0].squeeze()))
        queue.append((img_id[0], detections))

        imgs += 1
        if imgs % 10 == 0:
            print(f"\r{(imgs / (time.time() - start)):.2f} imgs/s \t \t", end="", flush=True)

            if imgs > MAX_RETRIEVED:
                break

    print(f"Infer Took {time.time() - start}", flush=True)


    start = time.time()
    print("Waiting for push to finish...", flush=True)
    stop = True

    for x in thds:
        x.join()

    print(f"Waiting for push to finish took: {time.time() - start}")

    # log_info(db, f"From DataLoaders Shuffle. n={MAX_RETRIEVED}")

    # start = time.time()
    # imgs = 0

    # for img, label in data_loader_shuffle:
    #     start_infer = time.time()
    #     detector.infer(np.array(img[0].squeeze()))
    #     # print(f"infer took: {time.time() - start_infer}s")
    #     imgs += 1
    #     if imgs % 10 == 0:
    #         # print(f"{imgs / (time.time() - start)} imgs/s")
    #         print(f"\r{(imgs / (time.time() - start)):.2f} imgs/s \t \t", end="")

    # print(f"Took {time.time() - start}")

    # log_info(db, f"From Dataset. n={MAX_RETRIEVED}")

    # start = time.time()
    # imgs = 0

    # for img, label in dataset:
    #     start_infer = time.time()
    #     detector.infer(img)
    #     # print(f"infer took: {time.time() - start_infer}s")
    #     imgs += 1
    #     if imgs % 10 == 0:
    #         # print(f"{imgs / (time.time() - start)} imgs/s")
    #         print(f"\r{(imgs / (time.time() - start)):.2f} imgs/s \t \t", end="")

    # print(f"Took {time.time() - start}")

    # print(f"Just inference:")

    # import cv2
    # img = cv2.imread("000000184679.jpg")

    # start = time.time()
    # imgs = 0

    # for i in range(MAX_RETRIEVED):
    #     detector.infer(img) # use the last image
    #     imgs += 1
    #     if imgs % 10 == 0:
    #         print(f"\r{(imgs / (time.time() - start)):.2f} imgs/s \t", end="", flush=True)

    # print(f"Just inference took {time.time() - start}")

def get_args():
    obj = argparse.ArgumentParser()

    # Run Config
    obj.add_argument('-dataset_mode', type=str, default="sequential")
    obj.add_argument('-model_name', type=str, default="frcnn-mobilenet")

    obj.add_argument('-clean',    type=bool,
                     default=os.environ.get('CLEAN', 'true').lower() in ('true', '1', 't'))

    params = obj.parse_args()

    return params

if __name__ == "__main__":
    args = get_args()

    start = time.time()
    # Needed for init_process_group
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'

    dist.init_process_group("gloo", rank=0, world_size=1)

    try:
        main(args)
    except Exception as e:
        print(e)
        print("Something went wrong, exiting...")
    except KeyboardInterrupt:
        stop = True
        print("Keyboard interrupt, exiting...")

    dist.destroy_process_group()

    query_file.close()
    print(f"Everything Took: {time.time() - start}")
    print("Done, bye.")
