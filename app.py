import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="AI Stock Dashboard", layout="wide")
st.title("AI-Powered Stock Dashboard")

# Sidebar input
st.sidebar.header("Stock Selection")
ticker = st.sidebar.text_input("Enter stock ticker (e.g., AAPL, NVDA, MSTR)", "AAPL")
date = st.sidebar.date_input("Select a date")

if ticker:
    st.write(f"### Analyzing {ticker} on {date}")

if ticker and date:
    stock = yf.Ticker(ticker)
    df = stock.history(interval="5m", start=date, end=date + pd.Timedelta(days=1))

    if not df.empty:
        st.success(f"Fetched {len(df)} records for {ticker}")
        st.dataframe(df.head())
    else:
        st.warning("No data found for this date.")

if not df.empty:
    high_row = df.loc[df['High'].idxmax()]
    low_row = df.loc[df['Low'].idxmin()]

    st.subheader("🔎 Key Levels")
    st.write(f"**High Price:** {high_row['High']:.2f} at {high_row.name}")
    st.write(f"**Low Price:** {low_row['Low']:.2f} at {low_row.name}")

    # Plot
    fig, ax = plt.subplots(figsize=(10,5))
    sns.lineplot(data=df, x=df.index, y="Close", ax=ax, label="Close Price")
    ax.axhline(high_row['High'], color="green", linestyle="--", label="Day High")
    ax.axhline(low_row['Low'], color="red", linestyle="--", label="Day Low")
    ax.legend()
    st.pyplot(fig)