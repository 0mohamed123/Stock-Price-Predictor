import pandas as pd
import numpy as np
import joblib
from model_trainer import train_model

def predict_new_data(model, scaler, new_data):
    
    new_data_scaled = scaler.transform(new_data)
    prediction = model.predict(new_data_scaled)
    return prediction[0]

if __name__ == "__main__":
    try:
        model = joblib.load("trained_model.pkl")
        scaler = joblib.load("scaler.pkl")
        print("Loaded existing model and scaler.")
    except FileNotFoundError:
        print("No saved model found, training a new one...")
        model, scaler = train_model()
        joblib.dump(model, "trained_model.pkl")
        joblib.dump(scaler, "scaler.pkl")
    
    new_sample = [[750, 730, 740, 50000000]]
    predicted_price = predict_new_data(model, scaler, new_sample)
    print(f"Predicted Closing Price: ${predicted_price:.2f}")