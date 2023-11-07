#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    # Define the Reddit API URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set a custom User-Agent to avoid too many requests issues
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    
    # Send a GET request to the subreddit's hot posts
    response = requests.get(url, headers=headers)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response to extract the titles of the first 10 posts
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        # If the subreddit is invalid or there's an issue, print None
        print(None)

if __name__ == '__main__':
    import sys


    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        top_ten(subreddit)
