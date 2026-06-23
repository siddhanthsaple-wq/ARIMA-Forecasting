import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from datetime import datetime

st.set_page_config(page_title="Indian Stock ARIMA Forecast", layout="wide")

st.title("ARIMA Stock Forecasting App")
st.write("Forecast Indian Stocks using ARIMA Model")

# User Input
ticker = st.text_input(
    "Enter NSE Stock Symbol (Example: RELIANCE.NS, TCS.NS, HDFCBANK.NS)",
    "RELIANCE.NS"
)

if st.button("Generate Forecast"):

    try:

        # Download 5 years of data
        data = yf.download(
            ticker,
            period="5y",
            auto_adjust=True
        )

        if data.empty:
            st.error("No data found.")
            st.stop()

        close_prices = data["Close"]

        st.subheader("Last 5 Years Data")
        st.dataframe(close_prices.tail())

        # ARIMA Model
        model = ARIMA(close_prices, order=(5,1,0))
        model_fit = model.fit()

        # Calculate months until June 2027
        today = datetime.today()
        target_date = datetime(2027, 6, 30)

        months = (
            (target_date.year - today.year) * 12
            + (target_date.month - today.month)
        )

        forecast = model_fit.forecast(steps=max(months, 12))

        forecast_df = pd.DataFrame({
            "Forecast Price": forecast
        })

        st.subheader("Forecast Values")
        st.dataframe(forecast_df)

        june_2027_price = forecast.iloc[-1]

        st.success(
            f"Estimated Forecast Price for June 2027: ₹{june_2027_price:.2f}"
        )

        # Plot

        fig, ax = plt.subplots(figsize=(12,6))

        ax.plot(
            close_prices.index,
            close_prices,
            label="Historical Prices"
        )

        future_dates = pd.date_range(
            start=close_prices.index[-1],
            periods=len(forecast)+1,
            freq="M"
        )[1:]

        ax.plot(
            future_dates,
            forecast,
            label="Forecast"
        )

        ax.set_title(f"{ticker} ARIMA Forecast")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")

        ax.legend()

        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")
