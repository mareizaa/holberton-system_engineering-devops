#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url,
                     headers={'User-Agent': 'marce1'},
                     allow_redirects=False,
                     params={'limit': 10})
    if r.status_code == 200:
        titles = (r.json().get("data").get("children"))
        for title in titles:
            print(title.get('data').get('title'))
    else:
        print(None)
