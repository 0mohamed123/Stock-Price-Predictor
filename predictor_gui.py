import sys
import numpy as np
import joblib
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class StockPredictorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.load_model()
    
    def initUI(self):
        self.setWindowTitle("Stock Price Predictor")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        self.high_input = QLineEdit(self)
        self.high_input.setPlaceholderText("Enter High Price")
        layout.addWidget(QLabel("High Price:"))
        layout.addWidget(self.high_input)
        
        self.low_input = QLineEdit(self)
        self.low_input.setPlaceholderText("Enter Low Price")
        layout.addWidget(QLabel("Low Price:"))
        layout.addWidget(self.low_input)
        
        self.open_input = QLineEdit(self)
        self.open_input.setPlaceholderText("Enter Open Price")
        layout.addWidget(QLabel("Open Price:"))
        layout.addWidget(self.open_input)
        
        self.volume_input = QLineEdit(self)
        self.volume_input.setPlaceholderText("Enter Volume")
        layout.addWidget(QLabel("Volume:"))
        layout.addWidget(self.volume_input)
        
        self.predict_button = QPushButton("Predict Closing Price", self)
        self.predict_button.clicked.connect(self.make_prediction)
        layout.addWidget(self.predict_button)
        
        self.result_label = QLabel("Predicted Price: ", self)
        layout.addWidget(self.result_label)
        
        self.setLayout(layout)
    
    def load_model(self):
        try:
            self.model = joblib.load("trained_model.pkl")
            self.scaler = joblib.load("scaler.pkl")
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "Model or Scaler not found! Train the model first.")
            sys.exit()
    
    def make_prediction(self):
        try:
            high = float(self.high_input.text())
            low = float(self.low_input.text())
            open_price = float(self.open_input.text())
            volume = float(self.volume_input.text())
            
            new_data = np.array([[high, low, open_price, volume]])
            new_data_scaled = self.scaler.transform(new_data)
            prediction = self.model.predict(new_data_scaled)[0]
            
            self.result_label.setText(f"Predicted Price: ${prediction:.2f}")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numeric values.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StockPredictorApp()
    window.show()
    sys.exit(app.exec())