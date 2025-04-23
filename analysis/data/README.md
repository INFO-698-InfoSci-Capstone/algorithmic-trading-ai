# 📊 Stocex Data Folder

This folder contains the data files used for the **Stocex: AI-Driven Algorithmic Trading** capstone project.

---

## 🧠 Purpose of the Study

To explore the impact of news sentiment and historical price movements on intraday stock forecasting using machine learning and time series models (FinBERT, Timegpt, etc.).

---

## 📁 Files in This Folder

### `sentiment_summary.csv`

| Column Name           | Description                                           | Format     |
|-----------------------|-------------------------------------------------------|------------|
| `Ticker`              | Stock ticker symbol (e.g., AAPL, MSFT)               | String     |
| `Mentions`            | Number of news articles the stock was mentioned in   | Integer    |
| `Avg Sentiment Score` | Average FinBERT sentiment score (0 = neg, 1 = pos)   | Float [0-1]|
| `Dominant Sentiment`  | Most frequent sentiment label                         | String     |

---

### `news_headlines.csv`

| Column Name     | Description                             | Format     |
|------------------|-----------------------------------------|------------|
| `title`          | Title of the news article               | String     |
| `description`    | Short summary of the article            | String     |
| `publishedAt`    | Date and time of publication            | YYYY-MM-DD |
| `source`         | Source (e.g., CNBC, Reuters)            | String     |

---


#### Inside each `*_price_history.csv`

| Column Name | Description             | Format     |
|-------------|-------------------------|------------|
| `Date`      | Trading date            | YYYY-MM-DD |
| `Price`     | Adjusted close price    | Float      |

---

## 📅 Data Status

- ✅ Generated dynamically from NewsAPI + yFinance
- ✅ Updated daily via Google Colab
- ❗ Forecast output and SEA markers to be added soon

---

## 🧾 License & Use

Data sources:  
- News: [NewsAPI.org](https://newsapi.org)  
- Prices: [Yahoo Finance](https://finance.yahoo.com)

Use for academic/non-commercial purposes only.

---

## 📬 Contact

**Sanjeevteja P** 
