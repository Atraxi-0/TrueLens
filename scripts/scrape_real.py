# scripts/scrape_real.py

from newspaper import Article, build
import pandas as pd
import time

# List of trusted Indian news URLs (homepage or national section)
urls = [
    'https://www.thehindu.com/news/national/',
    'https://www.ndtv.com/india',
]

real_articles = []

for url in urls:
    print(f"\n🔍 Building paper for: {url}")
    try:
        paper = build(url, memoize_articles=False)
        print(f"  ✅ Found {len(paper.articles)} articles")

        for i, article in enumerate(paper.articles[:30]):  # Limit per source
            try:
                article.download()
                article.parse()

                # Filter short or blank articles
                if article.text and len(article.text) > 300:
                    real_articles.append({
                        'title': article.title,
                        'text': article.text,
                        'label': 'real'
                    })
                    print(f"    ✔ ({i+1}) {article.title[:60]}...")
                time.sleep(1)
            except Exception as e:
                print(f"    ⚠️ Failed to parse article {i+1}: {e}")
    except Exception as e:
        print(f"  ❌ Failed to build paper for {url}: {e}")

# Save the scraped articles
if real_articles:
    df = pd.DataFrame(real_articles)
    df.to_csv("dataset/real_news.csv", index=False)
    print(f"\n✅ Saved {len(df)} real news articles to dataset/real_news.csv")
else:
    print("❌ No real news scraped.")
