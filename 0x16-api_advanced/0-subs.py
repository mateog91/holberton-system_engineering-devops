#!/usr/bin/python3
"""
    Module for task 0
"""
import requests


def number_of_subscribers(subreddit):
    """
    Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

    Args:
        subreddit (_type_): _description_
    Return:
    Number of subscribers. If not a valid subreddit, return 0.
    """

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'MyHolbertonAPI/0.0.1'}
    response = requests.get(url, headers=headers)
    content = response.json()
    data = content['data']
    return data.get('subscribers', 0)
