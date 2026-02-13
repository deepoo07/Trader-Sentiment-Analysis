import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Trader Performance vs Market Sentiment Dashboard")

# Load data
df = pd.read_csv("merged_df.csv")

# ---------------- Dataset Preview ----------------
st.subheader("Dataset Preview")
st.dataframe(df.head())

# ---------------- Sentiment Filter ----------------
sentiment = st.selectbox(
    "Select Market Sentiment",
    df["classification"].dropna().unique()
)

filtered_df = df[df["classification"] == sentiment]

# ---------------- PnL Chart ----------------
st.subheader("Average PnL by Sentiment")

pnl_chart = df.groupby("classification")["Closed PnL"].mean()

fig, ax = plt.subplots()
pnl_chart.plot(kind="bar", ax=ax)
st.pyplot(fig)

# ---------------- Trade Size Chart ----------------
st.subheader("Average Trade Size (Filtered Sentiment)")

size_chart = filtered_df.groupby("classification")["Size USD"].mean()

fig2, ax2 = plt.subplots()
size_chart.plot(kind="bar", ax=ax2)
st.pyplot(fig2)

# ---------------- Win Rate ----------------
st.subheader("Win Rate by Sentiment")

win_rate = df.groupby("classification")["Win Trade"].mean()

st.write(win_rate)