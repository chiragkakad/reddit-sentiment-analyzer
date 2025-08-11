# 📊 Reddit Sentiment Analyzer

A Streamlit web app that analyzes the sentiment of top Reddit posts for any subreddit and time frame.  
It uses **NLTK's VADER Sentiment Analyzer** to score posts and displays visual insights,.

## ✨ Features
- Fetches top Reddit posts for a selected time range (`day`, `week`, `month`, `year`, `all`).
- Calculates **average sentiment score**.
- Displays **sentiment distribution chart**.
- Shows **Top 5 Positive** and **Top 5 Negative** posts.
- Allows downloading results as CSV.

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/chiragkakad/reddit-sentiment-analyzer.git
   cd reddit-sentiment-analyzer
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in `.env`:

   ```
   REDDIT_CLIENT_ID=your_client_id
   REDDIT_CLIENT_SECRET=your_client_secret
   REDDIT_USER_AGENT=your_user_agent
   ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

5. Open the provided local URL in your browser.

---

## 🛠 Tech Stack

* **Python** (NLTK, pandas, matplotlib, wordcloud)
* **Streamlit** for the web interface
* **PRAW** for Reddit API

---