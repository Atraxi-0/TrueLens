import os
import csv
import feedparser
from datetime import datetime

# Define RSS feeds from Times of India
feeds = {
    "India": "https://timesofindia.indiatimes.com/rssfeeds/-2128936835.cms",
    "World": "https://timesofindia.indiatimes.com/rssfeeds/296589292.cms",
    "Science": "https://timesofindia.indiatimes.com/rssfeeds/-2128672765.cms",
    "Tech": "https://timesofindia.indiatimes.com/rssfeeds/5880659.cms"
}

articles = []

print()

# Parse each feed
for category, url in feeds.items():
    print(f"🔎 Parsing feed: {category}")
    feed = feedparser.parse(url)

    for entry in feed.entries:
        print(f"  🔗 {entry.title.strip()}")

        article = {
            "title": entry.title.strip(),
            "link": entry.link.strip(),
            "published": entry.get("published", "").strip(),
            "category": category,
            "source": "Times of India",
            "label": "real"
        }

        articles.append(article)

# Ensure directory exists
output_dir = os.path.join("data", "real")
os.makedirs(output_dir, exist_ok=True)

# Save to CSV
if articles:
    output_path = os.path.join(output_dir, "toi_news.csv")
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=articles[0].keys())
        writer.writeheader()
        writer.writerows(articles)

    print(f"\n💾 Saved {len(articles)} articles to {output_path}")
else:
    print("\n⚠️ No articles found to save.")
