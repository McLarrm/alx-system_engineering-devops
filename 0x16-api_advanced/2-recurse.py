#!/usr/bin/python3
"""
recursive function that queries the Reddit API
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    # Define the Reddit API URL for the subreddit with a specified 'after' parameter
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"

    # Set a custom User-Agent to avoid too many requests issues
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Send a GET request to the subreddit's hot posts
    response = requests.get(url, headers=headers)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response to extract the titles of the posts
        data = response.json()
        posts = data['data']['children']

        # Append the titles of these posts to the hot_list
        for post in posts:
            hot_list.append(post['data']['title'])

        # Check if there are more pages to fetch
        after = data['data']['after']
        if after is not None:
            # Recursively call the function to fetch the next page
            return recurse(subreddit, hot_list, after)
        else:
            # No more pages to fetch, return the hot_list
            return hot_list
    else:
        # If the subreddit is invalid or there's an issue, return None
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
