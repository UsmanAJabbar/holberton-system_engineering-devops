#!/usr/bin/python3
"""Returns the titles of the 10 hottest posts on a specific subreddit"""


def top_ten(subreddit):
    """
    ---------------
    METHOD: top_ten
    ---------------
    Description:
        Finds and returns the top 10 posts on
        a specific subreddit.
    Args:
        @subreddit: subreddit to ping
    Notes:
        If the subreddit is invalid, this function
        returns None, else, upto 10 posts.
    """
    from requests import get as r_get

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    data = r_get(url, allow_redirects=False, headers={'User-agent': ''}).json()

    out = ([title['data']['title'] for title in data['data']['children'][:10]]
           if data.get('data') and data['data'].get('children')
           is not None else None)

    ([print(titles) for titles in out] if out is not None else print(None))
