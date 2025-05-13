<p align="center">
  <img src="https://raw.githubusercontent.com/INFO-698-InfoSci-Capstone/algorithmic-trading-ai/main/Poster/stocex_logo.png" alt="Stocex Logo" width="250"/>
</p>

# Stocex 🧠📈  
**AI-Powered Intraday Trading Assistant using News + TimeGPT**

---

## 🧩 What is Stocex?

**Stocex** is a lightweight yet powerful Python script that scans daily financial headlines, scores their sentiment using FinBERT, detects affected stocks, fetches intraday price data, forecasts future prices using TimeGPT, and generates actionable trade signals.

---

## ⚙️ How It Works

> 🧠 Just run one script and everything happens automatically.

### 🔁 Pipeline Overview

1. **Fetch News (via NewsAPI):**  
   Get yesterday’s market headlines from Bloomberg, WSJ, CNBC, etc.

2. **Sentiment Scoring (FinBERT):**  
   Use HuggingFace FinBERT to score each headline (positive, neutral, negative)

3. **Company Detection (spaCy):**  
   Extract mentioned companies using Named Entity Recognition (NER)

4. **Ticker Mapping:**  
   Match company names to real stock tickers (e.g., Apple → AAPL)

5. **Intraday Price Data (yfinance):**  
   Download 5-minute historical data for last 30 days for each ticker

6. **Forecasting (TimeGPT-1):**  
   Forecast next 12 bars (1 hour) using Nixtla’s TimeGPT-1 API

7. **Signal Generation:**  
   Combine sentiment and forecast direction:
   - ✅ BUY = positive sentiment & forecast up
   - ❌ SELL = negative sentiment & forecast down
   - 🤝 HOLD = neutral or conflicting signals

8. **Output:**  
   Prints signal for each ticker (e.g., `AAPL: BUY`, `TSLA: HOLD`)

---

## 🌐 Streamlit Dashboard

```bash
streamlit run src/app.py
```

### Dashboard Highlights
- 🧠 **Sentiment Overview** — histogram, top tickers, volatility-return scatter
- 📰 **News Headlines** — filter by date and ticker
- 🔮 **1-Hour Simulated Forecast** — based on average sentiment
- 🤖 **AI Q&A Tab** — ask: "highest sentiment", "return of TSLA", etc.
- 🌓 **Dark Mode** toggle for better visual comfort

---

## 📦 Dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

Includes:
- `yfinance`, `transformers`, `spacy`, `requests`, `pandas`, `torch`

---

## ▶️ Usage

```bash
python Stocex.py
```

---

## 🖥️ Sample Output

```
📅 News fetched for 2025-04-10
🔍 Tickers mentioned: ['AAPL', 'TSLA', 'NCLH']
📈 Forecasted next 12 bars with TimeGPT
✅ AAPL: BUY (positive news + price ↑)
❌ TSLA: SELL (negative news + price ↓)
🤝 NCLH: HOLD (neutral news or mixed forecast)
```

---

## 📜 License

Licensed under the **GNU General Public License v3.0**  
See [LICENSE.txt](LICENSE.txt) for full details.

---

## 📬 Contact

📧 **stocex.team@gmail.com**  
> _“Let the AI read the news, so you can read the profits.”_ 💹
