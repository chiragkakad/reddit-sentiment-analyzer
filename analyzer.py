import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Ensure NLTK resources are available
nltk.download("vader_lexicon", quiet=True)

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(posts):
    """
    Analyze sentiment for a list of posts.
    :param posts: list of dicts with 'title' key
    :return: list of dicts with added sentiment score
    """
    results = []
    for post in posts:
        score = sia.polarity_scores(post["title"])["compound"]
        post["sentiment"] = score
        results.append(post)
    return results

def get_top_posts_by_sentiment(posts, positive=True, count=5):
    """
    Get top N positive or negative posts.
    """
    sorted_posts = sorted(posts, key=lambda x: x["sentiment"], reverse=positive)
    return sorted_posts[:count]
