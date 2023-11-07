#!/usr/bin/python3
"""
Function that queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    # Define the Reddit API URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    # Set a custom User-Agent to avoid too many requests issues
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Send a GET request to the subreddit's about page
    response = requests.get(url, headers=headers)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response to extract the number of subscribers
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # If the subreddit is invalid or there's an issue, return 0
        return 0

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(subscribers)
