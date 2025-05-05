# Weekly/Bi-Weekly Log

## Prompts
Following the [Rose/Bud/Thorn](https://www.panoramaed.com/blog/rose-bud-thorn-activity-and-worksheet#:~:text=%22Rose%2C%20Bud%2C%20Thorn%22%20is%20a%20mindful%20design%2D,day%2C%20week%2C%20or%20month.) model:

## 🗓 Date:
## Week 1 – April 11, 2025

⏱ Number of hours:
~18–20 hours
(News fetching, ticker extraction, FinBERT sentiment analysis, yfinance integration for historical price data)

🌹 Rose – Highlight of the week:
Successfully created an automated pipeline to fetch financial news from NewsAPI, extract S&P 500 stock tickers using NLP (SpaCy), and analyze sentiment using FinBERT. The pipeline produced a meaningful output showing dominant sentiment and sentiment score per mentioned stock ticker — a huge milestone for the Stocex project!
We have also filtered and selected tickers having average sentiment score of >0.98.
Additonally we have saved data into csv for future use in SEA analysis.

🌱 Bud – Looking forward to:
Integrating forecasting with Chronos or TimeGPT, and combining those forecasts with sentiment scores to build real-time trading signals. There's a strong potential here to generate actionable insights based on news-driven movement, and this will be crucial in moving towards the live signal dashboard.

🥀 Thorn – Challenges:
Slight ambiguity in matching company names from the headlines with tickers (string matching wasn’t always perfect).

Loading chronos-ts failed locally — had to revert to TimeGPT for now.

Fetching intraday data from yfinance is slightly slow and sometimes flaky for certain tickers.

💭 Additional thought:
Make sure to modularize the functions and package the full Steps 1–4 logic cleanly, so this pipeline can run automatically every morning. Also consider caching or saving results (e.g., yesterday’s news and sentiment_df) locally or in S3 to avoid reprocessing. This will help scale better when moving toward the alert and visualization stages.



## 🗓 Date:
## Week 2 – April 18, 2025

⏱ Number of hours:
~20–22 hours
(Finalizing forecasting integration, SEA preparation, Streamlit prototype creation)

🌹 Rose – Highlight of the week:
Integrated TimeGPT forecasting into the Stocex pipeline, enabling next 7-day price predictions based on historical stock data.
Successfully processed the full workflow: fetching financial news ➡️ extracting companies ➡️ mapping to tickers ➡️ fetching intraday prices ➡️ resampling to daily ➡️ forecasting with TimeGPT.
Designed and tested a basic version of **Superposed Epoch Analysis (SEA)** to align stock price behavior relative to positive sentiment news events.
Prepared and prototyped a **Streamlit app** layout for future deployment.
Saved structured outputs into CSVs for future visualization and backtesting.

🌱 Bud – Looking forward to:
Deploying the first working version of the Stocex app on **Streamlit Cloud**.
Adding multi-ticker SEA visualization support and dynamic parameter adjustments (window size, sentiment threshold) directly in the UI.
Exploring real-time alert integration (e.g., sending daily stock signals based on news + forecast combination).

🥀 Thorn – Challenges:
Some tickers fetched from NewsAPI headlines (e.g., non-S&P 500 small caps) caused yfinance fetch failures — added error handling but still needs optimization.
Chronos library setup encountered conflicts with local environment versions (especially on Colab), needed fallback to direct TimeGPT API.
SEA testing limited by the availability of recent news events (many were future-dated or lacked sufficient price history).

💭 Additional thought:
Modularizing the code into clear functional scripts has proven very beneficial for scaling.
Need to finalize automatic sentiment labeling (positive/negative) for better SEA differentiation.
Deployment is ready — only **final step pending** is pushing the app to Streamlit Cloud.
Focus next week: go live and refine visualizations for multi-ticker comparison.



## 🗓 Date:
## Week 3 – April 25, 2025
⏱ Number of hours: ~22–24 hours (Pipeline automation, Power BI visualization, Streamlit front-end)

🌹 Rose – Highlight of the week:
We successfully automated the full Stocex pipeline — it now fetches financial news daily, extracts tickers, runs sentiment analysis, and automatically selects the top 3 tickers with the highest sentiment scores for further processing. Additionally, we created Power BI visualizations to display sentiment trends and stock forecast insights, adding an extra layer of interactivity. The Streamlit front-end was also developed to show real-time sentiment, price forecasts, and SEA charts, giving us a functional dashboard ready for deployment and user testing.

🌱 Bud – Looking forward to:
We're excited to start working on our iShowcase poster for project presentation. This will include our system architecture, methodology (News → NLP → Sentiment → Forecast), and demo screenshots. We'll also refine the multi-ticker UI on Streamlit, possibly integrating a real-time signal alert feature and adding customization options (e.g., choose tickers, set sentiment threshold).

🥀 Thorn – Challenges:
Some minor issues in aligning Power BI outputs with the CSV pipeline structure. Also, automating the top-3 ticker logic required careful handling to avoid duplicate or weak-sentiment stocks. Streamlit rendering of interactive charts can lag occasionally — we may need to optimize layout and loading.

💭 Additional thought:
The automated pipeline and visual layer have now reached a stable MVP stage. Next steps include refining the poster and polishing the front-end for iShowcase. Consider adding a ticker search feature in Streamlit and a log file system to track daily pipeline results for transparency and debugging.



## 🗓 Date:
## Week 4 – May 02, 2025
⏱ Number of hours: ~23–25 hours (Streamlit deployment, Power BI finalization, GitHub updates)

🌹 Rose – Highlight of the week:
We finalized and deployed the Streamlit app showcasing sentiment-based forecasting, SEA visualizations, and price trends. We also completed and published our Power BI dashboards for sentiment analysis. All code and results were uploaded to GitHub, with the project README and HTML notebook versions updated for transparency and reproducibility.

🌱 Bud – Looking forward to:
Refining the visual polish of our Streamlit app and poster for the final iShowcase presentation. We’re planning to add features like ticker search and forecast intervals. We're also considering logging pipeline results daily and enabling CSV download of signals directly from the app.

🥀 Thorn – Challenges:
While exporting and formatting the HTML notebook for GitHub, we encountered rendering inconsistencies with certain plots. Adjusting layout and responsiveness in Streamlit (especially SEA plots) required some trial and error. Power BI integration needed column remapping due to final pipeline structure changes.

💭 Additional thought:
The project has reached a stable, deployable state. The Streamlit app, GitHub repo, and Power BI dashboard are all linked and ready for demo. Final steps will focus on polishing the UI, testing signal reliability, and preparing a clear narrative for iShowcase.

---


---

