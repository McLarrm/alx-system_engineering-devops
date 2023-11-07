#!/usr/bin/python3
"""
recursive function that queries the Reddit API
"""

import requests
import re


def count_words(subreddit, word_list, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    # Define the Reddit API URL for the subreddit with a specified 'after' parameter
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"

    # Set a custom User-Agent to avoid too many requests issues
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Send a GET request to the subreddit's hot posts
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the JSON response to extract the titles of the posts
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        after = data['data']['after']
        if after:
            return count_words(subreddit, word_list, hot_list, after)
        else:
            return process_words(hot_list, word_list)
    else:
        return process_words(hot_list, word_list)

def process_words(hot_list, word_list):
    word_counts = {}
    for word in word_list:
        word_counts[word.lower()] = 0

    for title in hot_list:
        for word in word_list:
            word_count = len(re.findall(rf'\b{word}\b', title, re.IGNORECASE))
            word_counts[word.lower()] += word_count

    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_word_counts:
        if count > 0:
            print(f"{word}: {count}")

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [x.lower() for x in sys.argv[2].split()]
        count_words(subreddit, word_list)
