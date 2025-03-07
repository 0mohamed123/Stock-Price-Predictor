import pandas as pd

def preprocess_data(filename="stock_data.csv"):

    df = pd.read_csv(filename, skiprows=2)
    
    df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]
    
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')
    
    df = df.dropna()
    
    numeric_cols = ["Close", "High", "Low", "Open", "Volume"]
    df[numeric_cols] = df[numeric_cols].astype(float)
    
    df = df.sort_values(by="Date")
    
    print("Data preprocessing completed successfully!")
    return df

if __name__ == "__main__":
    df = preprocess_data()
    print(df.head())
