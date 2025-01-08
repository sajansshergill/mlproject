import os
import pickle
import sys
import dill
from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor #helps to create the pickel file
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'src')))
from exception import CustomException
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from logger import logging

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
    
    
'''
def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)
'''

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    model_report = {}

    for model_name in models:
        model = models[model_name]
        try:
            logging.info(f"Training model: {model_name}")
            
            # Handle potential GridSearchCV or RandomizedSearchCV errors for XGBRegressor
            if isinstance(model, XGBRegressor):
                # Manually fit the model without using GridSearchCV for XGBRegressor
                model.fit(X_train, y_train)
                predicted = model.predict(X_test)
                r2_square = r2_score(y_test, predicted)
                model_report[model_name] = r2_square
            else:
                # Use GridSearchCV for other models
                grid_search = GridSearchCV(model, param.get(model_name, {}), cv=3)
                grid_search.fit(X_train, y_train)
                best_model = grid_search.best_estimator_
                predicted = best_model.predict(X_test)
                r2_square = r2_score(y_test, predicted)
                model_report[model_name] = r2_square
        except Exception as e:
            logging.error(f"Error training model {model_name}: {str(e)}")
            model_report[model_name] = None  # In case of failure, we log the error and assign None

    return model_report

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)