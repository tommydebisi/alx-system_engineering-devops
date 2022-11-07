#!/usr/bin/python3
"""
    This script queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
        Gets the the number of subscribers for the given subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit \
                    /537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    res = requests.get(url, headers=headers)
    if not res:
        return 0

    return res.json().get('data').get('subscribers')
