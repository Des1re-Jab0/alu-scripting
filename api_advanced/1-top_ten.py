#!/usr/bin/python3
"""Module that queries the Reddit API for the top ten hot posts."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit.

    Prints OK (no newline) if the subreddit is invalid or unreachable.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0.0 (by /u/alu_student)"}
    params = {"limit": 10}
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False, timeout=10)
        if response.status_code != 200:
            print("OK", end="")
            return
        posts = response.json().get("data", {}).get("children", [])
    except (requests.RequestException, ValueError):
        print("OK", end="")
        return
    for post in posts[:10]:
        print(post.get("data", {}).get("title"))
