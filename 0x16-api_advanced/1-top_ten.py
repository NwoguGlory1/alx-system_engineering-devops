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
    - The the first 10 hot posts or None if the subreddit is invalid.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?show="all"&limit=10'
    .format(subreddit)

    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    try:
        top_ten = response.json()['data']['children']
        for post in top_ten:
            print(post['data']['title'])
    except KeyError:
        print("None")

