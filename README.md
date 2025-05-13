# 📈 **AAPL Stock Price Prediction – "*Buy low, sell high... maybe?*"** 💸
**Inspired by** real-world trading curiosity and a splash of data science energy.

![project-banner.png](project-banner.png)

## 🚀 **Project Overview**
Ever wondered if you could predict Apple Inc. (AAPL) stock prices just using historical data and a bit of machine learning magic? This project explores that idea using a Linear Regression model. 

We don't promise stock tips... but we do promise **data**, **plots**, and **insights**!

### 🎯 **Project Goal**
To predict the future closing price of AAPL stock using historical data and evaluate how well a simple linear regression model can do the job.

Two core modules:
* **Data Extraction**: Loads or fetches historical stock prices.
* **Prediction**: Applies Linear Regression to forecast and evaluate performance.

---

## 🧱 **Tech Stack**

- **Language**: Python 🐍
- **Data Source**: `yfinance` API
- **Libraries Used**:
  - `pandas`, `numpy`
  - `matplotlib`, `seaborn`
  - `scikit-learn`
- **Modeling Method**: LinearRegression from `scikit-learn`
- **Metrics**: MSE, MAE

---

## ⚙️ **Project Workflow**

### **1. 📥 Data Collection**
- Pulled historical AAPL data using the `yfinance` API
- Cached the results in `aapl.csv` to avoid repeated downloads
- Focused on columns like: `Open`, `Close`, `High`, `Low`, `Volume`

### **2. 📊 Exploratory Data Analysis (EDA)**
- Plot the `Close`, `High`, `Low`, `Open`, `Volume`.
- Used `pct_change()` to calculate daily returns
- Identified the **best** and **worst** return days
- Compared return distributions between:
  - Full historical period
  - COVID-19 pandemic period (2020–2021)
- Used **standard deviation** to visualize volatility and impact

Plots include:
- Distribution of returns over all time
- Distribution during the COVID crash
- Price trends over time

### **3. 🤖 Model Training & Evaluation**
- Trained a `LinearRegression` model using:
  - Features: `Prev Close`, `High-Low`, `Open-Close`, `Volume`, `MA10`, `MA20`, `MA50` prices
  - Target: `Close` price
- Evaluated using:
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)

---

## 📈 Sample Output

```text
Mean Squared Error (Training Set): 0.2356
Mean Absolute Error (Training Set): 0.1830

Mean Squared Error (Test Set): 2.9015
Mean Absolute Error (Test Set): 1.1050
```
> ⚠️ Despite the metrics showed how the predictions turned out to be quite good, but please don't bet your savings on this yet! 😉

## 📁 **File Structure**
```bash
📦 market-prediction/
├── extract_data.py              # Download/caching logic for AAPL stock data
├── market_prediction.ipynb      # Main notebook for analysis and modeling
├── aapl.csv                     # Saved dataset
├── project-banner.png           # README image banner
└── README.md                    # You’re reading it!
```

## 🧩 **Future Improvements**
* Try polynomial or multivariate regression.
* Predict % change in price rather than absolute close value
* Incorporate technical indicators (SMA, RSI, MACD)
* Expand to multiple stocks (e.g., S&P500)
* Add model explainability using SHAP or permutation importance

# 💬 **Contact**
New to ML, still learning the ropes — would love feedback, suggestions, or just to geek out about stocks and models! 📉📈

📧 [Gmail](andrhmdk@gmail.com)<br>
🔗 [LinkedIn](https://www.linkedin.com/in/hmdkien/)