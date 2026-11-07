#!/usr/bin/python3
"""Module that queries the Reddit API for the top ten hot posts."""
import requests
import sys


def top_ten(subreddit):
    """Print the first 10 hot post titles, or OK if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0.0 (by /u/alu_student)"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        sys.stdout.write("OK")
        return

    posts = response.json().get("data", {}).get("children", [])
    for post in posts:
        print(post.get("data", {}).get("title"))
