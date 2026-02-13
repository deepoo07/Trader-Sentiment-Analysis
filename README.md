# Trader Performance vs Market Sentiment Analysis

## Project Overview
This project analyzes the relationship between market sentiment and trader performance using historical trading data and the Fear & Greed Index. The objective is to understand whether trader profitability and behavior change under different market sentiment conditions and to identify behavioral patterns across traders.

The project combines data preprocessing, feature engineering, exploratory data analysis, statistical aggregation, clustering, and dashboard visualization to derive meaningful insights from trading activity data.

---

## Problem Statement
Financial markets are strongly influenced by sentiment-driven behavior. Traders often react differently during periods of fear, greed, or neutral sentiment. Understanding how sentiment affects trading performance and behavior can help platforms improve risk monitoring, personalization, and decision-making tools.

This project investigates:
- Performance variation across sentiment regimes
- Behavioral changes in trading activity
- Identification of trader archetypes
- Visualization of results through an interactive dashboard

---

## Dataset Description

### Fear & Greed Index Dataset
Contains daily market sentiment classification including:
- Timestamp
- Sentiment Value
- Sentiment Classification (Fear, Greed, Extreme Fear, Extreme Greed, Neutral)
- Date

### Historical Trading Dataset
Contains individual trade-level data including:
- Account (Trader ID)
- Execution Price
- Trade Size (USD and Tokens)
- Trade Direction (Buy / Sell)
- Timestamp
- Closed PnL
- Trade ID
- Fees
- Order Details

---

## Methodology

### Data Preprocessing
- Removed irrelevant columns  
- Converted timestamps to daily date format  
- Handled missing values and duplicates  
- Aligned sentiment and trading datasets using date-level merge  

### Feature Engineering
Created key performance and behavior metrics including:
- Daily trader PnL  
- Win rate calculation  
- Trade size analysis  
- Trade frequency metrics  
- Long vs Short directional behavior  
- Trades per day trend  

Note: Leverage was not included as the dataset did not contain margin or leverage-related fields.

---

### Exploratory Data Analysis
Analyzed performance and behavior across sentiment categories:
- Average PnL by sentiment  
- Win rate by sentiment  
- Trade size behavior across sentiment regimes  
- Trading activity trends over time  

---

### Behavioral Clustering
Applied K-Means clustering to identify trader archetypes based on:
- Average PnL  
- Trade Size  
- Win Consistency  

---

### Dashboard Development
Developed a Streamlit dashboard to provide interactive visualization of:
- Performance metrics across sentiment  
- Trade behavior patterns  
- Summary performance tables  

---

## Key Insights

### Performance vs Sentiment
Trader profitability varied across sentiment regimes. Extreme sentiment periods often showed higher volatility in performance.

### Trading Activity Trends
Daily trading activity increased significantly in recent periods, indicating increased trader participation and potential market volatility.

### Behavioral Segmentation
Clustering revealed distinct trader groups based on profitability consistency and trade size patterns.

---

## Strategy Recommendations
- Implement sentiment-aware risk monitoring systems  
- Provide personalized trading tools based on trader behavior clusters  
- Use sentiment signals to build adaptive trading alerts  
- Extend analysis using real-time market data integration  

---

## Technology Stack
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  
- Streamlit  
- Jupyter Notebook  

---

## Project Structure

```
Trader-Sentiment-Analysis/
│
├ Trader_Sentiment_Analysis_Final.ipynb
├ dashboard.py
├ README.md
├ fear_greed_index.csv
├ historical_data.csv
│
├ outputs/
│   ├ pnl_chart.png
│   ├ trades_per_day.png
│   └ dashboard_preview.png
```
