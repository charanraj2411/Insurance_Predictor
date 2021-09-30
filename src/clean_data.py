import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from get_data import read_params

def find_category(path):
    df_train = pd.read_csv(path,sep=",")
    categorical_features=[feature for feature in df_train.columns if df_train[feature].dtypes=='O']
    return categorical_features



def encode_cat_data(categorical_features , processed_data_path , clean_data_path):
    df = pd.read_csv(processed_data_path,sep=",")

    lbl_encoders={}

    for feature in categorical_features:
        lbl_encoders[feature]=LabelEncoder()
        df[feature]=lbl_encoders[feature].fit_transform(df[feature])

    df.to_csv(clean_data_path,sep=",",index=False,encoding="utf-8")


def clean_data(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    test_clean_data_path = config["clean_data"]["test_path"]
    train_clean_data_path = config["clean_data"]["train_path"]
    
    categorical_features = find_category(train_data_path)

    encode_cat_data(categorical_features , train_data_path , train_clean_data_path)
    encode_cat_data(categorical_features , test_data_path , test_clean_data_path)


if __name__=="__main__":
    args= argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args=args.parse_args()
    data = clean_data(config_path=parsed_args.config)