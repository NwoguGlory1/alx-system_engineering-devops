#!/usr/bin/python3
"""
Defines a function for retrieving
a list containing the titles of all hot articles
for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], count=None, after=None):
    """
    Retrieve a  list containing the titles of all hot articles
    given subreddit.

    Args:
    - subreddit (str): The name of the subreddit

    Returns:
    - The list or None if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            params={"count": count, "after": after}
            )
    if response.status_code >= 400:
        return None
    else:
        data = response.json()
        posts = data.get("data").get("children")
        after = data.get("data").get("after")
        count = data.get("data").get("count")
        for post in posts:
            hot_list.append(post.get("data").get("title"))

        if not after:
            return hot_list
        else:
            return recurse(subreddit, hot_list, count, after)
