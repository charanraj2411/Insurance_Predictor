import numpy as np
from sklearn.preprocessing import StandardScaler
import os
import yaml
import joblib

params_path = "params.yaml"

sc=StandardScaler()

def read_params(config_path):
    with open (config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def model_create():
    config = read_params(params_path)
    model_dir_path = config["webapp_model_dir"]
    model = joblib.load(model_dir_path)
    return model
    

def calc_output(data):
    data = list(data.values())
    input_values=np.array(data)
    input_values=input_values.reshape(1,-1)
    input_values = sc.fit_transform(input_values)
    model=model_create()
    y_pred=model.predict(input_values)
    return y_pred[0]
    



    