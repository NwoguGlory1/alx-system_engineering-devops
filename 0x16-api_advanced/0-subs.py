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
    - The number of subscribers, or 0 if the subreddit is invalid.
    """
    url = 'http://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(
            url, headers=headers, allow_redirects=False)

    if (not response.ok):
        return 0
    data = response.json().get('data').get('subscribers')
    return data
