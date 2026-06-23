# ARIMA Stock Forecasting App

## Project Overview

This project is a web-based stock forecasting application developed using Streamlit and Python. The application retrieves the last five years of historical stock market data from Yahoo Finance and applies the ARIMA (AutoRegressive Integrated Moving Average) time series forecasting model to predict future stock prices.

The user can enter any Indian stock listed on the National Stock Exchange (NSE), and the application generates:

* Historical stock price data
* ARIMA-based forecast values
* Forecasted stock price for June 2027
* Interactive visualization of historical and forecasted prices

---

## Objectives

* Collect historical stock data using Yahoo Finance.
* Apply the ARIMA forecasting model to financial time series data.
* Predict future stock prices up to June 2027.
* Display forecast results numerically and graphically.
* Deploy the application using GitHub and Streamlit Cloud.

---

## Technologies Used

| Technology               | Purpose                    |
| ------------------------ | -------------------------- |
| Python                   | Programming Language       |
| Streamlit                | Web Application Framework  |
| Yahoo Finance (yfinance) | Historical Stock Data      |
| Pandas                   | Data Manipulation          |
| Matplotlib               | Data Visualization         |
| Statsmodels              | ARIMA Model Implementation |
| GitHub                   | Version Control            |
| Streamlit Cloud          | Application Deployment     |

---

## Methodology

### Step 1: Data Collection

Historical stock data for the last five years is collected using the Yahoo Finance API through the yfinance library.

### Step 2: Data Preparation

The closing prices of the selected stock are extracted and cleaned for analysis.

### Step 3: ARIMA Model

The ARIMA model is applied to the closing price series.

ARIMA consists of:

* AR (Auto Regression)
* I (Integrated Differencing)
* MA (Moving Average)

Model Format:

ARIMA(p,d,q)

Where:

* p = Number of autoregressive terms
* d = Degree of differencing
* q = Number of moving average terms

### Step 4: Forecasting

The trained model forecasts future stock prices up to June 2027.

### Step 5: Visualization

The application displays:

* Historical Stock Prices
* Forecasted Stock Prices
* Estimated Price for June 2027

---

## Features

* Supports any NSE-listed stock.
* Downloads live data from Yahoo Finance.
* Generates ARIMA-based forecasts.
* Displays forecast values in tabular format.
* Visualizes forecast using graphs.
* User-friendly web interface.

---

## Sample Stock Symbols

| Company             | Symbol       |
| ------------------- | ------------ |
| Reliance Industries | RELIANCE.NS  |
| TCS                 | TCS.NS       |
| HDFC Bank           | HDFCBANK.NS  |
| ICICI Bank          | ICICIBANK.NS |
| Infosys             | INFY.NS      |
| SBI                 | SBIN.NS      |

---

## Installation

Clone the repository:

git clone https://github.com/yourusername/arima-stock-forecast.git

Navigate to the project directory:

cd arima-stock-forecast

Install required packages:

pip install -r requirements.txt

Run the application:

streamlit run app.py

---

## Project Structure

arima-stock-forecast/

│

├── app.py

├── requirements.txt

├── README.md

│

└── assets/

---

## Future Improvements

* Auto-ARIMA parameter optimization
* Multiple stock comparison
* Seasonal ARIMA (SARIMA)
* LSTM-based forecasting
* Portfolio forecasting dashboard
* Risk and volatility analysis

---

## Conclusion

This project demonstrates the practical application of time series forecasting in financial markets using the ARIMA model. By leveraging historical stock price data and statistical forecasting techniques, the application provides investors and researchers with a simple tool for analyzing potential future stock price movements.

---

## Author

Siddhanth Saple

B.Com (Banking & Insurance)

Finance & Investment Enthusiast

Asset Management Aspirant
