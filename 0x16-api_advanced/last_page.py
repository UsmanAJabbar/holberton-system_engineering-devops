#!/usr/bin/python3
"""Returns a list of titles... this time, recursively"""


def recurse():
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

    url = 'https://www.reddit.com/r/deadsubs/hot.json?after=t3_1njucr'.format()
    data = r_get(url, allow_redirects=False, headers={'User-agent': ''}).json()

    print(type(data['data']['after']), data['data']['before'])

    # out = ([title['data']['title'] for title in data['data']['children'][:10]]
           # if data.get('data') and data['data'].get('children')
           # is not None else None)


recurse()
