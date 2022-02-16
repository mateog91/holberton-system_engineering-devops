#!/usr/bin/python3
"""
    Module for task 0
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit.
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyHolbertonAPI/0.0.1'}
    param = {'after': after}
    response = requests.get(url, headers=headers, params=param)

    if (response.status_code == 200):
        content = response.json()
        children = content['data']['children']
        add_list(hot_list, children)
        after = content['data']['after']
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    return None


def add_list(hot_list, c_list):
    """
    Recursive function that appends to hotlists and pops from c_list

    Args:
        hot_list (list): list with titles to append
        c_list (list): input list to acces the title
    """
    if not c_list:
        return
    last = c_list.pop()
    hot_list.append(last['data']['title'])
    add_list(hot_list, c_list)
