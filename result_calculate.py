import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle

sc=StandardScaler()

def model_create(input_values):
    Pkl_Filename = "Pickle_RL_Model.pkl"
    with open(Pkl_Filename, 'rb') as file:  
        model = pickle.load(file)
    return model
    

def calc_output(data):
    data = list(data.values())
    input_values=np.array(data)
    input_values=input_values.reshape(1,-1)
    input_values = sc.fit_transform(input_values)
    model=model_create(input_values)
    y_pred=model.predict(input_values)
    return y_pred[0]
    



    