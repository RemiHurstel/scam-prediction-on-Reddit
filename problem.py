import os
import numpy as np
from glob import glob
import pandas as pd
from sklearn.model_selection import ShuffleSplit
import rampwf as rw
from rampwf.workflows.sklearn_pipeline import SKLearnPipeline
from rampwf.workflows.sklearn_pipeline import Estimator
# --------------------------------------------------
####### Challenge title

problem_title = "Scam prediction on Reddit"

# --------------------------------------------------

_target_column_name = 'label'
_prediction_label_names = [0, 1]

Predictions = rw.prediction_types.make_multiclass(
    label_names=_prediction_label_names
    )

workflow = rw.workflows.Estimator()

score_types = [
    rw.score_types.F1Above(name='f1_above')
]

def get_cv(X, y):
    cv = ShuffleSplit(n_splits=2, test_size=0.30, random_state=42)
    return cv.split(X, y)

def _get_data(path, f_name):
    dataset = pd.read_csv(os.path.join(path, 'data', f_name))
    return dataset

def get_train_data(path=""):
    f_name = "train.csv"
    return _get_data(path, f_name)

def get_test_data(path=""):
    f_name = "test.csv"
    return _get_data(path, f_name)
