import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("stock_data.csv", skiprows=2)

df.columns = ["Date", "Close", "High", "Low", "Open", "Volume"]

df["Date"] = pd.to_datetime(df["Date"])

df = df.sort_values(by="Date")

print(df.head())

plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Close"], label="closing price", color='blue')
plt.xlabel("the date")
plt.ylabel("price (USD)")
plt.title("TSLA stock closing price over time")
plt.legend()
plt.xticks(rotation=45)
plt.show()