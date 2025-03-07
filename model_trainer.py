import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

def train_model(filename="stock_data.csv"):
    
    df = pd.read_csv(filename, skiprows=2)
    df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    df = df.dropna()
    df = df.sort_values(by="Date")
    
    X = df[["High", "Low", "Open", "Volume"]]
    y = df["Close"]
    
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print(f"Model trained successfully!\nMean Absolute Error: {mae:.4f}\nRoot Mean Squared Error: {rmse:.4f}")
    
    return model, scaler

if __name__ == "__main__":
    model, scaler = train_model()