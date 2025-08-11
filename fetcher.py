import os
import praw
from dotenv import load_dotenv

load_dotenv()

def get_reddit_client():
    """Initialize and return a Reddit API client using PRAW."""
    return praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT", "Reddit Sentiment Analyzer")
    )

def fetch_top_posts(subreddit_name, time_filter="day", limit=50):
    """
    Fetch top posts from a subreddit.
    :param subreddit_name: str, name of subreddit
    :param time_filter: str, e.g., "day", "week", "month", "year", "all"
    :param limit: int, number of posts to fetch
    :return: list of dicts containing post title, score, url
    """
    reddit = get_reddit_client()
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for post in subreddit.top(time_filter=time_filter, limit=limit):
        posts.append({
            "title": post.title,
            "score": post.score,
            "url": f"https://reddit.com{post.permalink}"
        })

    return posts
