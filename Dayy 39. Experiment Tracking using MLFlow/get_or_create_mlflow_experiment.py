import os
import mlflow
import pathlib

mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))

def get_experiment_id(name):
    
    # Check if experiment exists, if not create it
    exp = mlflow.get_experiment_by_name(name)
    
    if exp is None:
        exp_id = mlflow.create_experiment(name)
        return exp_id
    return exp.experiment_id

# Example usage
print(get_experiment_id("mario_wario"))
