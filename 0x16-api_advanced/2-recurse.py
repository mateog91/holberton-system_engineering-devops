#!/usr/bin/python3
"""
    Module for task 0
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyHolbertonAPI/0.0.1'}
    response = requests.get(url, headers=headers)
    if (response.status_code == 200):
        content = response.json()
        children = content['data']['children']
        lenght = len(children)
        recurse2(hot_list, children)
        print(hot_list)
    else:
        print(None)

def recurse2(hot_list, c_list):
    if not c_list:
        return
    last = c_list.pop()
    hot_list.append(last['data']['title'])
    recurse2(hot_list, c_list)
