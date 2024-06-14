"""
module for finding the shortest path between two Wikipedia articles using BFS
"""

from collections import deque
from wiki_fetcher import fetch_wiki_article, extract_links

def find_shortest_path(start_title, end_title, max_depth=500, link_limit=50):
    visited = set()
    queue = deque([(start_title, [start_title])])
    depth = 0
    while queue:
        if depth > max_depth:
            return None
        depth += 1
        current_title, path = queue.popleft()
        if current_title == end_title:
            return path
        if current_title not in visited:
            visited.add(current_title)
            try:
                html_content = fetch_wiki_article(current_title)
                links = extract_links(html_content)[:link_limit]
                for link in links:
                    if link not in visited:
                        queue.append((link, path + [link]))
            except Exception as e:
                print(f"error fetching or parsing the article '{current_title}': {e}")
    return None