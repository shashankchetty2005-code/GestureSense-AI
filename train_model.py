import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("dataset.csv",header=None)

X = data.iloc[:,:-1]
y = data.iloc[:,-1]

model = RandomForestClassifier()

model.fit(X,y)

joblib.dump(model,"gesture_model.pkl")

print("Model trained successfully")