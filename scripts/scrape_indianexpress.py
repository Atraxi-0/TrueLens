import requests
from bs4 import BeautifulSoup
import csv
import time
from datetime import datetime

BASE_URL = "https://indianexpress.com"
SECTIONS = ["india", "explained", "world"]
PAGES = 5  # Number of pages per section

headers = {
    'User-Agent': 'Mozilla/5.0'
}

articles = []

def get_article_text(link):
    try:
        res = requests.get(link, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        article_body = soup.find("div", class_="full-details")
        if not article_body:
            return ""
        return " ".join(p.get_text(strip=True) for p in article_body.find_all("p"))
    except Exception as e:
        print(f"⚠️ Failed to extract article: {link} ({e})")
        return ""

for section in SECTIONS:
    for page in range(1, PAGES + 1):
        url = f"{BASE_URL}/section/{section}/page/{page}/"
        print(f"🔎 Scraping {url}")
        try:
            res = requests.get(url, headers=headers)
            soup = BeautifulSoup(res.text, "html.parser")
            links = soup.find_all("a", class_="title")
            print(f"  ✅ Found {len(links)} articles")

            for link in links:
                href = link.get("href")
                if not href.startswith("http"):
                    href = BASE_URL + href
                title = link.get_text(strip=True)
                text = get_article_text(href)
                if text:
                    articles.append({
                        "title": title,
                        "url": href,
                        "text": text,
                        "label": "real",
                        "source": "Indian Express",
                        "date_scraped": datetime.now().isoformat()
                    })
                time.sleep(1)  # Be polite to their server
        except Exception as e:
            print(f"❌ Error scraping page {page} of {section}: {e}")

# Save to CSV
output_file = "data/indianexpress_real_news.csv"
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=articles[0].keys())
    writer.writeheader()
    writer.writerows(articles)

print(f"\n💾 Saved {len(articles)} articles to {output_file}")
