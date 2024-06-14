"""
module for fetching and parsing through Wikipedia articles
"""

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://en.wikipedia.org"

def fetch_wiki_article(title):
    title = title.replace(' ', '_')
    url = f"{BASE_URL}/wiki/{title}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"failed to fetch article: {title}")

def extract_links(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    for link in soup.find_all("a", href=True):
        href = link.get("href")
        if href.startswith("/wiki/") and not href.startswith("/wiki/Special:"):
            article_title = href.split("/wiki/")[1]
            if ':' not in article_title and '#' not in article_title:
                links.append(article_title.replace('_', ' '))
    return links