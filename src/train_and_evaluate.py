# load the train and test
# train the algo
# save the metrics, params

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from urllib.parse import urlparse
from get_data import read_params
import argparse
import joblib
import json
import pickle
import os


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2



def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["clean_data"]["test_path"]
    train_data_path = config["clean_data"]["train_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]
    max_depth = config["estimators"]["DecisionTreeRegressor"]["params"]["max_depth"]
    min_samples_split = config["estimators"]["DecisionTreeRegressor"]["params"]["min_samples_split"]
    model_dir = config["model_dir"]

    target = config["base"]["target_col"]

    train = pd.read_csv(train_data_path,sep=",")
    test  = pd.read_csv(test_data_path,sep=",")

    train_y = train[target]
    test_y = test[target]

    train_x = train.drop(target,axis=1)
    test_x = test.drop(target,axis=1)

    sc = StandardScaler()
    train_x = sc.fit_transform(train_x)
    test_x = sc.transform(test_x)   

    regressor = DecisionTreeRegressor(max_depth=max_depth, min_samples_split=min_samples_split)
    regressor.fit(train_x, train_y)

    predicted_qualities = regressor.predict(test_x)
    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

    # print("RMSE value is ", rmse)
    # print("MAE value is ", mae)
    # print("R2 value is ", r2)

    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]

    with open(scores_file,"w") as f:
        scores = {
            "rmse": rmse,
            "mae": mae,
            "r2" : r2
        }
        json.dump(scores, f, indent=4)

    with open(params_file,"w") as f:
        params = {
            "max_depth": max_depth,
            "min_samples_split": min_samples_split
        }
        json.dump(params, f, indent=4)

    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")

    joblib.dump(regressor, model_path)




if __name__=="__main__":
    args= argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args=args.parse_args()
    data = train_and_evaluate(config_path=parsed_args.config)
