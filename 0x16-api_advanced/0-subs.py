#!/usr/bin/python3
"""Returns the number of subs a subscribers a specific subreddit has"""


def number_of_subscribers(subreddit):
    """
    -----------------------------
    METHOD: number_of_subscribers
    -----------------------------
    Description:
        Returns the number of subscribers in a
        specific subreddit.
    Args:
        @subreddit: subreddit to ping
    Notes:
        If the subreddit is invalid, this function
        returns a 0, else, the number of subs
    """
    from requests import get as r_get

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    sub = r_get(url, allow_redirects=False, headers={'User-agent': ''}).json()

    subs_count = sub['data']['subscribers'] if 'data' in sub else 0

    return subs_count
