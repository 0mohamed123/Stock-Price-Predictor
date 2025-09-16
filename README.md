# 📈 Stock Price Predictor

## 📌 Overview
This project aims to predict stock prices using historical financial data and machine learning models. The system allows users to preprocess financial data, train predictive models, and generate stock price forecasts. A simple GUI is also included for user-friendly interaction with the predictor.

## 📊 Dataset
- **Source:** stock_data.csv (provided in the repository).  
- **Content:** Historical stock price data (Date, Open, High, Low, Close, Volume).  
- **Target:** Predict future stock prices based on past trends.  

## ⚙️ Project Workflow
1. **Data Fetching:**  
   `fetch_data.py` – Retrieves and stores stock data.  

2. **Data Preprocessing:**  
   `data_preprocessor.py` – Cleans and preprocesses the dataset for training.  

3. **Exploratory Data Analysis:**  
   `explore_data.py` – Performs EDA and visualization of trends.  

4. **Model Training:**  
   `model_trainer.py` – Trains machine learning models on the stock dataset.  

5. **Prediction:**  
   `predictor.py` – Generates predictions from the trained model.  

6. **GUI Application:**  
   `predictor_gui.py` – Provides a graphical interface for users to input data and view predictions.  

## 🤖 Technologies & Libraries
- Python  
- Pandas & NumPy  
- Scikit-learn  
- Matplotlib & Seaborn  
- Tkinter (for GUI)  

## 📈 Results
- Models provide stock price trend predictions with reasonable accuracy.  
- Performance metrics include RMSE, MSE, and R² Score.  

## 📂 Project Structure
Stock-Price-Predictor/
│── data_preprocessor.py # Data preprocessing

│── explore_data.py # Exploratory Data Analysis

│── fetch_data.py # Data fetching script

│── model_trainer.py # Model training

│── predictor.py # Stock price prediction

│── predictor_gui.py # GUI for prediction

│── stock_data.csv # Historical stock data

│── README.md # Project documentation

│── requirements.txt # Dependencies

## 🚀 Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/0mohamed123/Stock-Price-Predictor.git
   cd Stock-Price-Predictor
   ```
2. Install dependencies:
   ```bash
   pip install sickit-learn matplotlib numpy pandas pyqt
   ```
3. Run model training:
   ```bash
   python model_trainer.py
   ```
4. Run predictor:
   ```bash
   python predictor.py
   ```
5. Launch GUI:
   ```bash
   python predictor_gui.py
   ```

## 🛠️ Requirements
numpy
pandas
scikit-learn
matplotlib
seaborn
pyqt

## 👨‍💻 Author
Mohamed Kasm

## 📜 License
This project is licensed under the MIT License.
