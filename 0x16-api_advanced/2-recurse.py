#!/usr/bin/python3
"""Returns a list of titles... this time, recursively"""


def recurse(sub, hot=[], next=""):
    """
    ---------------
    METHOD: recurse
    ---------------
    DESCRIPTION:
        Returns a list of titles from a
        specific subreddit.
    Args:
        @subreddit: subreddit to ping
    Notes:
        If the subreddit is invalid, this function
        returns None, else, all of the post titles.
    """
    from requests import get as r_get

    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(sub, next)
    data = r_get(url, allow_redirects=False, headers={'User-agent': ''}).json()
    out = ([title['data']['title'] for title in data['data']['children'][:]]
           if data.get('data') and data['data'].get('children')
           is not None else None)

    if out is not None:
        hot += out
        next = data['data']['after']
        return recurse(sub, hot, next) if next is not None else hot
