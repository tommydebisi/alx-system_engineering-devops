#!/usr/bin/python3
"""
    This script queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    returns a list containing the titles of all hot articles
    for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit \
                    /537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    params = {'after': after}
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    if res.status_code == 200:
        for index in range(len(res.json().get('data').get('children'))):
            hot_list.append(res.json().get('data').get(
                'children')[index].get('data').get('title'))

        if res.json().get('data').get('after') is not None:
            return recurse(subreddit, hot_list, res.json()
                           .get('data').get('after'))
        else:
            return hot_list
    else:
        return None
