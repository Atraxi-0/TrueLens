import feedparser
import csv
from datetime import datetime
import os

RSS_FEED_URL = "https://factly.in/category/fake-news/feed/"
OUTPUT_PATH = "data/fake/factly_fake_news.csv"

def scrape_factly_rss():
    print("🔎 Fetching Factly Fake News RSS Feed...")
    feed = feedparser.parse(RSS_FEED_URL)
    articles = []

    for entry in feed.entries:
        title = entry.title.strip()
        summary = entry.summary.strip()
        link = entry.link
        date = entry.published if 'published' in entry else str(datetime.now())

        # Combine title and summary as 'text' (for AI model)
        content = f"{title}. {summary}"

        if content:
            articles.append({
                "title": title,
                "summary": summary,
                "url": link,
                "date": date,
                "text": content,
                "label": "FAKE"
            })
            print(f"  ✅ {title[:60]}...")

    if not articles:
        print("❌ No articles found.")
        return

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    with open(OUTPUT_PATH, "w", newline='', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=articles[0].keys())
        writer.writeheader()
        writer.writerows(articles)

    print(f"\n💾 Saved {len(articles)} articles to {OUTPUT_PATH}")

if __name__ == "__main__":
    scrape_factly_rss()
