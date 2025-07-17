import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    print("[INFO] Opening Alt News...")
    driver.get("https://www.altnews.in/latest")
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".td-ss-main-content .td-module-container"))
    )

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    article_elements = driver.find_elements(By.CSS_SELECTOR, ".td-ss-main-content .td-module-container a")[:10]
    article_urls = [elem.get_attribute("href") for elem in article_elements if elem.get_attribute("href")]

    print(f"[INFO] Found {len(article_urls)} articles")

    articles_data = []

    for url in article_urls:
        print(f"[INFO] Scraping: {url}")
        driver.get(url)
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        title_tag = soup.find("h1", class_="entry-title")
        title = title_tag.text.strip() if title_tag else "No Title"

        content_tag = soup.find("div", class_="td-post-content")
        content = content_tag.get_text(separator="\n").strip() if content_tag else "No Content"

        articles_data.append({"title": title, "content": content, "url": url})

    output_path = "../data/real/altnews_articles.csv"
    with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
        fieldnames = ["title", "content", "url"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for article in articles_data:
            writer.writerow(article)

    print(f"[SUCCESS] Scraped {len(articles_data)} articles and saved to {output_path}")

finally:
    driver.quit()
