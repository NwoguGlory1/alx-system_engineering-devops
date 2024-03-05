#!/usr/bin/python3
"""
Defines a function for retrieving
number of subreddit subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
    - subreddit (str): The name of the subreddit

    Returns:
    - int: The number of subscribers, or 0 if the subreddit is invalid.
    """

    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    response = requests.get(
            url,  headers={'User-Agent': 'My-User-Agent'}, allow_redirects=False
            )

    if response.status_code >= 300:
        return 0
    else:
        data = response.json()
        return data['data']['subscribers']
