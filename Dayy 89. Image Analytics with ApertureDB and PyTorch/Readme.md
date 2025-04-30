## Object Detection Model Evaluation Pipeline with ApertureDB and PyTorch 📸

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&style=flat-square)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-%26_Torchvision-orange?logo=pytorch&style=flat-square)](https://pytorch.org/)
[![ApertureDB](https://img.shields.io/badge/ApertureDB-Data_Platform-yellowgreen?style=flat-square)](https://www.aperturedata.io/)
[![Dataset](https://img.shields.io/badge/Dataset-COCO_on_ApertureDB-blueviolet?style=flat-square)](https://cocodataset.org/#home)
[![100DaysOfCode](https://img.shields.io/badge/100DaysOfDataScience-Day_89-brightgreen?style=flat-square)](https://www.100daysofcode.com/)

<img width="1318" alt="pipeline" src="https://github.com/user-attachments/assets/07b84625-2bdf-49a6-8d01-e6249f731eb0" />

*Fig 1: End-to-end pipeline leveraging ApertureDB for data retrieval, storing inference results, and evaluating model performance.*

## 🎯 Project Goal: Building an MLOps Evaluation Cycle with ApertureDB

Welcome to Day 89 of my #100DaysOfDataScience challenge! This project dives into a practical **Machine Learning Operations (MLOps)** workflow, demonstrating how to evaluate **Object Detection** models using **PyTorch/Torchvision** integrated with **ApertureDB**. We leverage ApertureDB not just as a data source (hosting the COCO dataset), but as a central hub for storing model predictions and performing evaluation queries.

**The Mission:**
1.  **Connect & Query:** Access the COCO image dataset hosted on a public ApertureDB instance.
2.  **Data Loading:** Efficiently load images into a **PyTorch Dataset** directly from ApertureDB queries.
3.  **Inference:** Run pre-trained object detection models (Faster R-CNN variations, RetinaNet) on the dataset images.
4.  **Store Predictions:** Push the model-generated bounding boxes back into ApertureDB, linked to the original images and tagged with the model source.
5.  **Evaluate Performance:** Use ApertureDB's query capabilities (`RegionIoU`) to calculate Intersection over Union (IoU) between ground truth boxes and model predictions *within the database*.
6.  **Aggregate & Store Score:** Calculate an average IoU score per image and then a global performance score for the model, storing this metadata back into ApertureDB.

This project showcases how specialized databases like ApertureDB can streamline the ML model evaluation cycle, keeping data, predictions, and performance metrics tightly integrated.

---

## ✨ Key Features & Concepts Mastered

*   **ApertureDB Integration:**
    *   Connecting to a remote ApertureDB instance (`Connector.Connector`).
    *   Crafting complex **JSON queries** (`FindImage`, `FindBoundingBox`, `AddBoundingBox`, `RegionIoU`, `AddEntity`, `DeleteBoundingBox`) using constraints, references (`_ref`), connections (`is_connected_to`), and result specifications.
    *   Leveraging `aperturedb.PyTorchDataset` to seamlessly feed query results (images) into a PyTorch `DataLoader`.
*   **PyTorch Object Detection:**
    *   Utilizing pre-trained models from `torchvision.models.detection` (Faster R-CNN ResNet50, Faster R-CNN MobileNetV3, RetinaNet ResNet50).
    *   Performing inference (`model.eval()`, `model(image)`) on images loaded via the custom dataset.
    *   Preprocessing images for Torchvision models (BGR->RGB, transpose, normalization, batch dim).
    *   Postprocessing detections (filtering by confidence score, extracting boxes, labels, scores).
*   **MLOps Evaluation Cycle:**
    *   Implementing a full loop: Data Retrieval -> Inference -> Store Results -> Evaluate -> Store Metrics.
    *   Calculating **Intersection over Union (IoU)** using ApertureDB's `RegionIoU` command to compare ground truth vs. predicted bounding boxes.
    *   Computing per-image and global average IoU scores, considering label matching.
*   **Data Handling & Scripting:**
    *   Using `cv2` (OpenCV) and `PIL` for image loading/display.
    *   Implementing **multithreading** (`threading`) to parallelize the process of pushing detection results and calculating IoU scores back to ApertureDB for efficiency.
    *   Structuring inference logic (`infer.py`) and the main evaluation/push pipeline (`infer_and_push_to_aperturedb.py`).
    *   Using `argparse` for script configuration (model selection, cleanup flag).

---

## 🛠️ Tech Stack: The Tools of the Trade

*   **Core Platform:** ApertureDB Cloud Instance (hosting COCO dataset)
*   **Client Library:** `aperturedb` Python Package (v0.15.19+ used in examples)
*   **ML Framework:** PyTorch, `torchvision.models.detection`
*   **Object Detection Models:** Faster R-CNN (ResNet50 FPN, MobileNetV3 Large 320 FPN), RetinaNet (ResNet50 FPN) - Pre-trained on COCO.
*   **Evaluation Metric:** Intersection over Union (IoU)
*   **Programming Language:** Python 3.8+
*   **Supporting Libraries:** OpenCV (`cv2`), Pillow (`PIL`), NumPy, `pickle` (for COCO classes), `threading`, `argparse`, `time`.
*   **Environment:** Jupyter Notebook, Python Scripts (for batch processing - `infer.py`, `infer_and_push_to_aperturedb.py`).

---

## 🗺️ The Workflow: Evaluating Models with ApertureDB

This project follows a structured MLOps evaluation pipeline, detailed across the provided files:

1.  **Setup & Connection (Task 1):**
    *   Install the `aperturedb` package.
    *   Establish a connection to the COCO dataset instance on ApertureDB Cloud using `Connector.Connector`.
    *   Verify connection with a `GetStatus` query.

2.  **Data Exploration & Dataset Creation (Task 2):**
    *   Query ApertureDB to find specific images (`FindImage` with `id` constraint) and their associated ground truth bounding boxes (`FindBoundingBox` linked via `image_ref`).
    *   Define a query to select a subset of images (e.g., 1000 images with `license >= 0`).
    *   Instantiate `aperturedb.PyTorchDataset` using the database connection and the image query. This allows lazy loading of images directly from the DB into PyTorch.
    *   Wrap the dataset in a PyTorch `DataLoader` for efficient batching and multiprocessing during inference.

3.  **Inference & Visualization (`infer.py`):**
    *   Define a `BboxDetector` class in `infer.py` to encapsulate model loading (`torchvision.models.detection`), image preprocessing (resizing via ApertureDB query operations or cv2/torch), inference (`model(image)`), and drawing bounding boxes on the output image.
    *   Test inference on sample images using different pre-trained models (`frcnn-resnet`, `frcnn-mobilenet`, `retinanet`) and visualize the detected objects with bounding boxes and confidence scores.
    *   Benchmark inference speed for single images and throughput using the `DataLoader`.

![image](https://github.com/user-attachments/assets/0bb87aad-3187-4e96-aff5-b55495297698)

*Fig 2: Example output of Faster R-CNN MobileNet on a tennis image, showing detected objects, boxes, and confidence.*

4.  **Pushing Predictions to ApertureDB (`infer_and_push_to_aperturedb.py`):**
    *   This script iterates through the `DataLoader`.
    *   For each image, it runs inference using the chosen model (`BboxDetector.infer`).
    *   It constructs an `AddBoundingBox` query for each confident detection (> 0.5 threshold), including the `label`, bounding box `rectangle` coordinates, and properties like `source` (model name) and `confidence`.
    *   Uses **multithreading** (`threading.Thread` with a queue) to push these `AddBoundingBox` queries to ApertureDB in parallel, improving throughput. Optionally includes a `--clean` flag to delete previous predictions from the same model source using `DeleteBoundingBox`.

5.  **Evaluating Performance using IoU (Task 4 & 5):**

      ![iou](https://github.com/user-attachments/assets/9ea44cd7-69ce-4e1a-99d1-b72c1ea87afe)

    *   Define a `compare_bboxes` function that takes an image ID and model name.
    *   Inside this function, craft a **complex ApertureDB query**:
        *   `FindImage` by ID (`_ref: 1`).
        *   `FindBoundingBox` for ground truth (`source == "ground_truth"`, `image_ref: 1`, `_ref: 2`).
        *   `FindBoundingBox` for model predictions (`source == model_name`, `image_ref: 1`, `_ref: 3`).
        *   `RegionIoU` command comparing the ground truth set (`roi_1: 2`) with the prediction set (`roi_2: 3`).
    *   Process the `RegionIoU` results: For each ground truth box, find the predicted box with the maximum IoU *and* matching label. Sum these maximum IoU values and average them over the number of ground truth boxes for that image to get a per-image score.
    *   **Global Score Calculation (Task 5):**
        *   Query ApertureDB to get all image IDs that have predictions stored for the target model.
        *   Use **multithreading** again to call `compare_bboxes` for *all* these image IDs in parallel.
        *   Aggregate the per-image scores to calculate a final average (global) IoU score for the model.

![graph](https://github.com/user-attachments/assets/81560995-b717-43cc-87b2-669d2faf3092)
*Fig 3: Conceptual diagram showing how Images, Ground Truth BBoxes, and Predicted BBoxes are related in ApertureDB, enabling the IoU query.*

6.  **Storing Performance Metrics (Task 6):**
    *   Construct an `AddEntity` query to create a new entity (e.g., class `ObjectDetectionModel-codealong`) representing the evaluated model.
    *   Store properties like `model_name` and the calculated `global_score`.
    *   Use `if_not_found` to avoid duplicates.
    *   Crucially, use `connect` to link this new model entity back to the images used in the evaluation dataset, preserving provenance. (Note: The provided output shows a permissions error for this step, indicating write access was needed).

---

## 💡 Key Insights & Advantages of This Approach

*   **ApertureDB as an MLOps Hub:** This project demonstrates ApertureDB's potential beyond just data storage. It acts as a central repository for ground truth, model predictions, *and* performance metrics, keeping the entire evaluation cycle integrated.
*   **In-Database Evaluation:** Calculating IoU via `RegionIoU` directly within ApertureDB can be more efficient than pulling all bounding boxes to the client, especially for large datasets. It leverages the database's computational capabilities.
*   **Seamless PyTorch Integration:** `aperturedb.PyTorchDataset` provides a convenient bridge, allowing standard PyTorch training/inference loops to consume data directly from complex database queries.
*   **Model Comparison Framework:** By storing predictions tagged by model name and calculating global scores, this pipeline provides a solid framework for comparing the performance of different object detection models on the same dataset.
*   **Scalability through Parallelism:** Using `threading` for pushing results and running evaluations significantly speeds up processing for larger datasets.

![Screenshot 2025-04-30 192644](https://github.com/user-attachments/assets/9b871993-2867-4b3d-90e3-c4314c93b1ab)

![Screenshot 2025-04-30 192747](https://github.com/user-attachments/assets/79267764-c573-4563-a9cc-220e7c4bb462)

*Fig 4: Example view of the ApertureDB interface, showing data distribution which includes Images and Bounding Boxes.*

---

*Day 89 of #100DaysOfDataScience successfully built an integrated object detection evaluation pipeline, demonstrating the powerful synergy between PyTorch for modeling and ApertureDB for data management and in-database evaluation. A solid step into practical MLOps! - Vatsal Parikh*
