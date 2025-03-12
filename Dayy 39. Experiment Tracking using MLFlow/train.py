# script for training a CNN classifier 

from config import PROCESSED_IMAGES_DIR, MODELS_DIR
import tensorflow.keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from dagshub import dagshub_logger
import os
import mlflow
import dagshub
from src.get_or_create_mlflow_experiment import get_experiment_id

def get_datasets(validation_ratio=0.2, target_img_size=64, batch_size=32):
    """
    Train/valid/test split based on this SO answer:
    https://stackoverflow.com/questions/42443936/keras-split-train-test-set-when-using-imagedatagenerator
    """
    train_datagen = ImageDataGenerator(rescale = 1./255,
                                       zoom_range=[0.5, 1.5],
                                       validation_split=validation_ratio)

    valid_datagen = ImageDataGenerator(rescale=1./255, 
                                       validation_split=validation_ratio)

    test_datagen = ImageDataGenerator(rescale = 1./255)

    training_set = train_datagen.flow_from_directory(f"{PROCESSED_IMAGES_DIR}/train",
                                                     target_size = (target_img_size, target_img_size),
                                                     color_mode="grayscale",
                                                     batch_size = batch_size,
                                                     class_mode = "binary",
                                                     shuffle=True,
                                                     subset="training")

    valid_set = valid_datagen.flow_from_directory(f"{PROCESSED_IMAGES_DIR}/train",
                                                  target_size = (target_img_size, target_img_size),
                                                  color_mode="grayscale",
                                                  batch_size = batch_size,
                                                  class_mode = "binary",
                                                  shuffle=False,
                                                  subset="validation")

    test_set = test_datagen.flow_from_directory(f"{PROCESSED_IMAGES_DIR}/test",
                                                target_size = (target_img_size, target_img_size),
                                                color_mode="grayscale",
                                                batch_size = batch_size,
                                                class_mode = "binary")

    return training_set, valid_set, test_set

def get_model(input_img_size, lr):
    """
    Returns a compiled model. 
    Architecture is fixed, inputs change the image size and the learning rate.
    """ 
    # Initializing 
    model = Sequential()

    # 1st conv. layer
    model.add(Conv2D(32, (3, 3), input_shape = (input_img_size, input_img_size, 1), activation = "relu"))
    model.add(MaxPooling2D(pool_size = (2, 2)))

    # 2nd conv. layer
    model.add(Conv2D(32, (3, 3), activation = "relu")) 
    model.add(MaxPooling2D(pool_size = (2, 2)))

    # 3nd conv. layer
    model.add(Conv2D(64, (3, 3), activation = "relu")) 
    model.add(MaxPooling2D(pool_size = (2, 2)))

    # Flattening
    model.add(Flatten())

    # Full connection
    model.add(Dense(units = 64, activation = "relu"))
    model.add(Dropout(0.5))
    model.add(Dense(units = 1, activation = "sigmoid"))

    model.compile(optimizer = tensorflow.keras.optimizers.Adam(learning_rate=lr),
                    loss = "binary_crossentropy", 
                    metrics = ["accuracy"])

    return model

if __name__ == "__main__":
    
    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))

    IMG_SIZE = 128
    LR = 0.001
    EPOCHS = 5
    


    training_set, valid_set, test_set = get_datasets(validation_ratio=0.2,
                                                     target_img_size=IMG_SIZE,
                                                     batch_size=32)
    model = get_model(IMG_SIZE, LR)
    
    mlflow.tensorflow.autolog()
    with mlflow.start_run(experiment_id = get_experiment_id('mario_wario')):
      # # Single parameter
      # mlflow.log_param("img_size", IMG_SIZE)

      # # Multiple parameters
      # mlflow.log_params({
      #     "img_size": IMG_SIZE,
      #     "learning_rate": LR,
      #     "epochs": EPOCHS
      # })

      # # Single metric
      # mlflow.log_metric("test_set_loss", test_loss, step=1)


      # # Multiple metrics
      # mlflow.log_metrics(
      #     {
      #         "test_set_loss": test_loss,
      #         "test_set_accuracy": test_accuracy,
      #     }
      # )

      # mlflow.log_artifact(MODELS_DIR)

      # mlflow.log_text("Here you can add general inforamtion about the run","run_info.txt")

      print("Training the model...")
      model.fit(training_set,
                validation_data=valid_set,
                epochs = EPOCHS)
      print("Training completed.")

      print("Evaluating the model...")
      test_loss, test_accuracy = model.evaluate(test_set)
      print("Evaluating completed.")
      print("Saving the model...")
      model.save(os.path.join(MODELS_DIR, 'my_model.keras'))
      print("done.")
    # with dagshub_logger() as logger:
    #     logger.log_metrics(loss=test_loss, accuracy=test_accuracy)
    #     logger.log_hyperparams({
    #         "img_size": IMG_SIZE,
    #         "learning_rate": LR,
    #         "epochs": EPOCHS
    #     })


