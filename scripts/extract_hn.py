#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Extract Cool HN Tech
# @raycast.mode silent

# Optional parameters:
# @raycast.icon 🚀
# @raycast.packageName Developer Tools

import concurrent.futures
import re
import time

import requests
from bs4 import BeautifulSoup
from utils import open_chat


def fetch_hackernews():
    response = requests.get("https://news.ycombinator.com/")
    soup = BeautifulSoup(response.text, "html.parser")

    stories = []
    titles = soup.find_all("span", class_="titleline")

    for title in titles[:30]:  # Get top 30 stories
        title_text = title.get_text().strip()
        link = title.find("a")["href"]
        stories.append({"title": title_text, "url": link})

    return stories


def fetch_article_content(story, timeout=5):
    """Fetch and extract brief content from the article URL"""
    try:
        # Skip URLs that are HN items or common non-article sites
        if story["url"].startswith("item?id=") or ".pdf" in story["url"].lower():
            return {"title": story["title"], "url": story["url"], "summary": ""}

        time.sleep(1)
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"
        }

        response = requests.get(story["url"], headers=headers, timeout=timeout)
        if response.status_code != 200:
            return {"title": story["title"], "url": story["url"], "summary": ""}

        soup = BeautifulSoup(response.text, "html.parser")

        # Try to get article content - looking for common article content patterns
        text = ""

        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.extract()

        # Try to find article content in common article containers
        article_elements = soup.select(
            "article, .article, .post-content, .entry-content, main"
        )

        if article_elements:
            text = article_elements[0].get_text(strip=True)
        else:
            # If no article container found, get the page text
            text = soup.get_text(strip=True)

        # Clean up the text
        text = re.sub(r"\s+", " ", text)

        # Get first ~500 characters as a summary
        summary = text[:500] + "..." if len(text) > 500 else text
        summary = summary.replace("{", "{{").replace(
            "}", "}}"
        )  # Escape braces for formatting

        return {"title": story["title"], "url": story["url"], "summary": summary}
    except Exception as e:
        return {
            "title": story["title"],
            "url": story["url"],
            "summary": f"Error fetching content: {str(e)}",
        }


def main():
    stories = fetch_hackernews()

    # Fetch article content in parallel
    enhanced_stories = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_story = {
            executor.submit(fetch_article_content, story): story for story in stories
        }
        for future in concurrent.futures.as_completed(future_to_story):
            enhanced_stories.append(future.result())

    # Format stories for prompt
    formatted_stories = []
    for story in enhanced_stories:
        story_text = f"Title: {story['title']}\nURL: {story['url']}"
        if story["summary"]:
            story_text += f"\nSummary: {story['summary']}"
        formatted_stories.append(story_text)

    story_text = "\n\n".join(formatted_stories)

    prompt = f"""Here is a list of the latest stories from Hacker News with summaries:

{story_text}

Please analyze these stories and extract the most interesting technological innovations, breakthroughs, or cool tech projects. Focus on:

1. Cutting-edge technology developments
2. Innovative projects or tools
3. Breakthrough research
4. Interesting technical solutions

Provide a concise summary of the 3-5 most noteworthy tech items, with brief explanations of why they're significant or innovative. When possible, include specific technical details from the article summaries."""

    open_chat(prompt, "Claude")


if __name__ == "__main__":
    main()
