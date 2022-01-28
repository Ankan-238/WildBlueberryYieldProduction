import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sklearn
from sklearn.ensemble import RandomForestRegressor

feat_cols=['clonesize',
 'osmia',
 'AverageOfUpperTRange',
 'AverageOfLowerTRange',
 'AverageRainingDays',
 'fruitset',
 'fruitmass',
 'seeds']

#Create a predicted funtion
X_test_rf_df=pd.read_csv(r"C:\Users\Ankan\Desktop\GMLP 2nd Jan\X_test_rf_df.csv", index_col=0)
rf_final= joblib.load(r"C:\Users\Ankan\Desktop\GMLP 2nd Jan\rf_bbry_tuned_model.pkl")

def predict_yield(attributes: np.ndarray):
    pred=rf_final.predict(attributes)
    print("Yield predicted: ")

    return (pred[0])


