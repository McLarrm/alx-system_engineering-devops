#!/usr/bin/python3
"""
recursive function that queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        result = recurse(subreddit)
        if result is not None:
            print(len(result))
        else:
            print("None")
