#!/usr/bin/python3
"""
    This script queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
        Prints the first 10 hot topics
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit \
                    /537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    res = requests.get(url, headers=headers)
    if res and res.status_code == 200:
        hot_children = res.json().get('data').get('children')
        for index in range(10):
            print(hot_children[index].get('data').get('title'))
    else:
        print(None)
