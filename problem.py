import os
from glob import glob
import pandas as pd
from sklearn.model_selection import ShuffleSplit
import rampwf as rw

# --------------------------------------------------
####### Challenge title

problem_title = "Scam prediction on Reddit"

# --------------------------------------------------


_prediction_label_names = [0, 1]

Predictions = rw.prediction_types.make_multiclass(
    label_names=_prediction_label_names
    )

workflow = rw.workflows.Classifier()

score_type_1 = rw.score_types.ROCAUC(name='auc')
score_type_2 = rw.score_types.Accuracy(name='acc')
score_type_3 = rw.score_types.F1Above(name='f1_above')

score_types = [
    # The official score combines the three scores with weights 1/4, 1/4, 2/4
    rw.score_types.Combined(
        name='combined', score_types=[score_type_1, score_type_2, score_type_3],
        weights=[1./4, 1./4, 2./4], precision=3),
]

_target_column_name = 'label'

def _get_data(path, f_name):
    dataset = pd.read_csv(os.path.join(path, 'data', f_name))
    X = dataset.drop([_target_column_name], axis=1)
    y = dataset[_target_column_name].values

    return X, y


def get_train_data(path="."):
    f_name = "train.csv"
    return _get_data(path, f_name)


def get_test_data(path="."):
    f_name = "test.csv"
    return _get_data(path, f_name)


def get_cv(X, y):
    cv = ShuffleSplit(n_splits=10, test_size=0.25, random_state=57)
    return cv.split(X, y)