# app.py
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# ✅ Page config
st.set_page_config(page_title="Stocex Dashboard", layout="wide")

# ✅ Theme toggle
st.sidebar.title("⚙️ Settings")
theme = st.sidebar.radio("Select Theme", ["Light Mode", "Dark Mode"])

is_dark = theme == "Dark Mode"

if is_dark:
    dark_css = """
    <style>
    body, .stApp {
        background-color: #121212;
        color: white;
    }
    .st-bb, .st-bd, .st-b8 {background-color: #1e1e1e;}
    .st-c0, .stMarkdown, .stTextInput > label, .css-10trblm {color: white !important;}
    .css-1v0mbdj, .css-12oz5g7 {background-color: #2e2e2e !important; color: white !important;}
    table, th, td {color: white !important; background-color: #1e1e1e !important;}
    </style>
    """
    st.markdown(dark_css, unsafe_allow_html=True)

# ✅ Header
st.markdown("""
<div style="background-color:#f5f5f5;padding:15px;border-radius:10px;margin-bottom:20px;">
    <h1 style="text-align:center;color:#0d47a1;">🚀 STOCEX Dashboard</h1>
    <p style="text-align:center;color:#424242;font-size:20px;">
        AI-Driven Intraday Stock Forecasting and Sentiment Analysis
    </p>
</div>
""", unsafe_allow_html=True)

# ✅ Load data
from pathlib import Path
sentiment_df = pd.read_csv("../analysis/data/sentiment_summary.csv")
news_df = pd.read_csv("../analysis/data/news_headlines.csv")
news_df["publishedAt"] = pd.to_datetime(news_df["publishedAt"]).dt.tz_localize(None)

scatter_df = pd.read_csv("../analysis/data/scatter_volatility_return.csv")
scatter_df.columns = scatter_df.columns.str.strip()
scatter_df["Average_Return"] = pd.to_numeric(scatter_df["Average_Return"], errors="coerce")
scatter_df["Volatility"] = pd.to_numeric(scatter_df["Volatility"], errors="coerce")
scatter_df = scatter_df.dropna(subset=["Average_Return", "Volatility"])
volatility_df = pd.read_csv("../analysis/data/stock_volatility_data.csv")
keyword_df = pd.read_csv("../analysis/data/news_keyword_frequency.csv")

# ✅ Sidebar filters
tickers = sorted(sentiment_df["Ticker"].unique())
selected_sentiment = st.sidebar.multiselect("Dominant Sentiment", sorted(sentiment_df["Dominant Sentiment"].unique()), default=sentiment_df["Dominant Sentiment"].unique())
min_mentions = st.sidebar.slider("Minimum Mentions", 1, 50, 1)
sentiment_range = st.sidebar.slider("Sentiment Score Range", 0.0, 1.0, (0.0, 1.0))

# ✅ Filtered data
filtered_sentiment_df = sentiment_df[(sentiment_df["Dominant Sentiment"].isin(selected_sentiment)) &
                                     (sentiment_df["Mentions"] >= min_mentions) &
                                     (sentiment_df["Avg Sentiment Score"].between(*sentiment_range))]

# ✅ Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🧠 Sentiment Overview", "📰 News Headlines", "📈 Historical Prices", "🔮 Forecast", "🤖 AI Q&A"])

# ------------------ TAB 1 ------------------ #
with tab1:
    st.header("📊 Sentiment Overview")

    st.subheader("📈 Sentiment Score Distribution")
    sentiment_hist = alt.Chart(sentiment_df).mark_bar().encode(
        x=alt.X("Avg Sentiment Score", bin=alt.Bin(maxbins=30), title="Average Sentiment Score"),
        y=alt.Y("count():Q", title="Number of Tickers"),
        tooltip=["count()"]
    ).configure(background="#121212" if is_dark else "white")
    st.altair_chart(sentiment_hist, use_container_width=True)

    st.subheader("📊 Top Mentioned Tickers")
    top_mentions = sentiment_df.sort_values("Mentions", ascending=False).head(15)
    mention_chart = alt.Chart(top_mentions).mark_bar().encode(
        x=alt.X("Mentions:Q"),
        y=alt.Y("Ticker:N", sort="-x"),
        tooltip=["Ticker", "Mentions"]
    ).configure(background="#121212" if is_dark else "white")
    st.altair_chart(mention_chart, use_container_width=True)

    st.subheader("📈 Volatility vs Return")
    scatter_plot = alt.Chart(scatter_df).mark_circle(size=100).encode(
        x=alt.X("Volatility", title="Annualized Volatility"),
        y=alt.Y("Average_Return", title="Annualized Return"),
        color=alt.Color("Ticker", legend=None),
        tooltip=["Ticker", "Volatility", "Average_Return"]
    ).interactive().configure(background="#121212" if is_dark else "white")
    st.altair_chart(scatter_plot, use_container_width=True)

    st.subheader("🗞️ Top Mentioned Keywords in News")
    keyword_bar = alt.Chart(keyword_df.head(15)).mark_bar(color="steelblue").encode(
        x=alt.X("Frequency:Q"),
        y=alt.Y("Keyword:N", sort="-x"),
        tooltip=["Keyword", "Frequency"]
    ).configure(background="#121212" if is_dark else "white")
    st.altair_chart(keyword_bar, use_container_width=True)

# ------------------ TAB 4 ------------------ #
with tab4:
    st.header(f"🔮 Forecasted Price Trend for {tickers[0]}")
    st.caption("This is a simulated 1-hour forecast using random walk. Replace with Chronos or TimeGPT for real results.")

    today = pd.to_datetime("today")
    forecast_dates = [today + pd.Timedelta(minutes=5 * i) for i in range(12)]  # next 1 hour
    start_price = sentiment_df["Avg Sentiment Score"].mean() * 100 + 100
    price_forecast = np.random.normal(0, 0.5, size=12).cumsum() + start_price
    ci_lower = price_forecast - np.random.uniform(1, 2, size=12)
    ci_upper = price_forecast + np.random.uniform(1, 2, size=12)

    forecast_df = pd.DataFrame({
        "Date": forecast_dates,
        "Forecast": price_forecast,
        "Lower": ci_lower,
        "Upper": ci_upper
    })

    base = alt.Chart(forecast_df).encode(x="Date:T")

    area = base.mark_area(opacity=0.3, color="lightblue").encode(
        y="Lower:Q",
        y2="Upper:Q"
    )

    line = base.mark_line(color="orange").encode(
        y="Forecast:Q",
        tooltip=["Date", "Forecast"]
    )

    forecast_chart = (area + line).configure(background="#121212" if is_dark else "white")
    st.altair_chart(forecast_chart, use_container_width=True)

# ------------------ TAB 5 ------------------ #
with tab5:
    st.header("🤖 Ask the App (AI Q&A)")
    question = st.text_input("Ask a question about stock sentiment, returns, or volatility:")
    if question:
        if "highest sentiment" in question.lower():
            top = sentiment_df.loc[sentiment_df['Avg Sentiment Score'].idxmax()]
            st.success(f"{top['Ticker']} has the highest sentiment score of {top['Avg Sentiment Score']:.2f}.")
        elif "most volatile" in question.lower():
            top_vol = volatility_df.loc[volatility_df['Volatility'].idxmax()]
            st.success(f"{top_vol['Ticker']} is the most volatile stock with volatility {top_vol['Volatility']:.2f}.")
        elif "return" in question.lower():
            import re
            match = re.search(r'return.*?([A-Z]+)', question)
            if match:
                tick = match.group(1)
                row = scatter_df[scatter_df['Ticker'] == tick]
                if not row.empty:
                    st.success(f"{tick}: Average_Return = {row.iloc[0]['Average_Return']:.2f}, Volatility = {row.iloc[0]['Volatility']:.2f}")
                else:
                    st.warning("Ticker not found in return data.")
            else:
                st.warning("Please specify a valid ticker symbol.")
        else:
            st.info("I can answer questions like: 'highest sentiment', 'most volatile stock', or 'return of AAPL'.")
