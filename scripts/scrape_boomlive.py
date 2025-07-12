# scripts/scrape_boomlive.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import re

BASE = "https://www.boomlive.in"
LIST_URL = BASE + "/fact-check?page={}"
HEADERS = {"User-Agent": "Mozilla/5.0"}
PAGES = 10  # increase as needed

def get_links(page):
    url = LIST_URL.format(page)
    print(f"\n🔎 Loading {url}")
    r = requests.get(url, headers=HEADERS, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        if re.search(r"/\d{4}/\d{2}/\d{2}/.+/", a["href"]):
            full = a["href"]
            if full.startswith("/"):
                full = BASE + full
            links.append(full)
    links = list(dict.fromkeys(links))  # dedupe
    print(f"  Found {len(links)} article links")
    return links

def parse_article(url):
    print(f"➡️ Parsing {url}")
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.find("h1")
        label = None
        for span in soup.find_all("span"):
            txt = span.get_text(strip=True)
            if txt.lower() in ("fake", "misleading", "true", "correct"):
                label = txt
                break
        date = soup.find("time")
        date = date.get("datetime") if date else None
        paragraphs = soup.find_all("p")
        content = "\n".join(p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 50)
        return {"url": url, "title": title.get_text(strip=True) if title else None, "label": label, "date": date, "content": content}
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    items = []
    for page in range(1, PAGES + 1):
        links = get_links(page)
        for link in links:
            art = parse_article(link)
            if art and art["content"]:
                items.append(art)
            time.sleep(1)

    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(items)
    df.to_csv("data/boomlive_articles.csv", index=False)
    print(f"\n✅ Saved {len(df)} items to data/boomlive_articles.csv")

if __name__ == "__main__":
    main()
