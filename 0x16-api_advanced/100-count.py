#!/usr/bin/python3
"""Returns a list of titles... this time, recursively"""


def count_words(sub, word_list, next="", keys={}):
    """
    -------------------
    METHOD: count_words
    -------------------
    DESCRIPTION:
        Returns the number of times keywords
        stored in word_list appeared
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

    # Create a dictionary storing the amount of times a specifc keyword was found in out
    for words in word_list:
        keys[words] = 0 if words not in keys else keys[words]
        for titles in out:
            if words in titles:
                keys[words] = keys[words] + 1

    if out is not None:
        next = data['data']['after']
        if next is not None:
            return count_words(sub, word_list, next, keys)
        else:
            if keys == {}:
                print()
            for k, v in sorted(keys.items(), reverse=True):
                if v != 0:
                    print(k + ":", v)
