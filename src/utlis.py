import pandas as pd
import numpy as np
import os
import sys

from sklearn.metrics import r2_score
from src.exception import CustomException
import pickle
import dill


def save_object(file_path, obj):
    '''
    This function saves a python object as a pickle file
    '''
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models):
    '''
    This function evaluates multiple machine learning models and returns their performance scores.
    '''
    try:
        model_report = {}
        for name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            r2_square = r2_score(y_test, y_pred)
            model_report[name] = r2_square
        return model_report
    except Exception as e:
        raise CustomException(e, sys)