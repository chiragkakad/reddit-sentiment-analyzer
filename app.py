import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from fetcher import fetch_top_posts
from analyzer import analyze_sentiment, get_top_posts_by_sentiment

st.set_page_config(page_title="Reddit Sentiment Analyzer", layout="wide")

st.title("📊 Reddit Sentiment Analyzer")

subreddit = st.text_input("Subreddit", value="cryptocurrency")
time_filter = st.selectbox("Time Filter", ["day", "week", "month", "year", "all"])
limit = st.slider("Number of posts", min_value=10, max_value=200, value=50, step=10)

if st.button("Analyze"):
    with st.spinner("Fetching and analyzing posts..."):
        posts = fetch_top_posts(subreddit, time_filter, limit)
        analyzed_posts = analyze_sentiment(posts)

        df = pd.DataFrame(analyzed_posts)

        # Average sentiment
        avg_sentiment = df["sentiment"].mean()
        st.metric("Average Sentiment", f"{avg_sentiment:.3f}")

        # Bar chart of sentiment distribution
        fig, ax = plt.subplots()
        ax.hist(df["sentiment"], bins=20, color="skyblue", edgecolor="black")
        ax.set_title("Sentiment Distribution")
        ax.set_xlabel("Sentiment Score")
        ax.set_ylabel("Number of Posts")
        st.pyplot(fig)

        # Top Positive
        st.subheader("Top 5 Positive Posts")
        st.table(pd.DataFrame(get_top_posts_by_sentiment(analyzed_posts, positive=True))[["title", "sentiment", "url"]])

        # Top Negative
        st.subheader("Top 5 Negative Posts")
        st.table(pd.DataFrame(get_top_posts_by_sentiment(analyzed_posts, positive=False))[["title", "sentiment", "url"]])

        
        # Download CSV
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", csv, f"{subreddit}_sentiment.csv", "text/csv")
