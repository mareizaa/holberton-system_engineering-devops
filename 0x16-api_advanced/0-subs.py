#!/usr/bin/python3
"""Queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    r = requests.get(url,
                     headers={'User-Agent': 'marce1'},
                     allow_redirects=False)
    if r.status_code == 200:
        return (r.json().get("data").get("subscribers"))
    return (0)
