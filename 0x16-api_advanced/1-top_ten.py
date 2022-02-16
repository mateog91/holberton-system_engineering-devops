#!/usr/bin/python3
"""
    Module for task 0
"""
import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit.
    """

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'MyHolbertonAPI/0.0.1'}
    response = requests.get(url, headers=headers)
    if (response.status_code == 200):
        content = response.json()
        children = content['data']['children']
        for child in children:
            print(child['data']['title'])
    else:
        print(None)
