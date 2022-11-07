#!/usr/bin/python3
"""
    This script queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Gets all the hot topics recursively and returns them
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit \
                    /537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    index = 0
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        hot_children = res.json().get('data').get('children')
        helper(hot_children, hot_list, index)
        return hot_list


def helper(hot_kids, hot_list, index):
    """
        helper function for recursive function
    """
    try:
        hot_list.append(hot_kids[index].get('data').get('title'))
    except IndexError:
        return

    helper(hot_kids, hot_list, index + 1)
