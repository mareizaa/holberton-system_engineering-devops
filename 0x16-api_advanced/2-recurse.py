#!/usr/bin/python3
"""
Queries the Reddit API and returns a list containing the titles
of all hot articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list containing the titles of all hot articles
    """
    if not after:
        url = 'https://www.reddit.com/r/{}/hot.json?'.format(subreddit)
    else:
        url = 'https://www.reddit.com/r/{}/hot.json?after={}'\
            .format(subreddit, after)

    r = requests.get(url,
                     headers={'User-Agent': 'marce1'}).json()

    if 'error' in r:
        return(None)
    else:
        result = r.get('data').get('children')
        for obj in result:
            hot_list.append(obj.get('data').get('title'))
        after = r.get('data').get('after')
        if not after:
            return hot_list
        return recurse(subreddit, hot_list, after)
