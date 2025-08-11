from fetcher import fetch_top_posts
from analyzer import analyze_sentiment, get_top_posts_by_sentiment

def main():
    subreddit = input("Enter subreddit name: ").strip()
    time_filter = input("Enter time filter (day, week, month, year, all): ").strip() or "day"
    limit = int(input("Enter number of posts to analyze: ").strip() or 50)

    posts = fetch_top_posts(subreddit, time_filter, limit)
    analyzed_posts = analyze_sentiment(posts)

    avg_sentiment = sum(p["sentiment"] for p in analyzed_posts) / len(analyzed_posts)
    print(f"\nAverage Sentiment Score: {avg_sentiment:.3f}")

    print("\nTop 5 Positive Posts:")
    for p in get_top_posts_by_sentiment(analyzed_posts, positive=True):
        print(f"{p['title']} ({p['sentiment']:.3f}) - {p['url']}")

    print("\nTop 5 Negative Posts:")
    for p in get_top_posts_by_sentiment(analyzed_posts, positive=False):
        print(f"{p['title']} ({p['sentiment']:.3f}) - {p['url']}")

if __name__ == "__main__":
    main()
