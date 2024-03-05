#!/usr/bin/python3
"""
Defines a function for retrieving
the titles of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Retrieve the titles of  the first 10 hot posts for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit

    Returns:
    - The first 10 hot posts or None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code >= 300:
        print("None")
    else:
        data = response.json()
        posts = data.get("data").get("children")
        for post in posts:
            print(post.get("data").get("title"))
