#!/usr/bin/python3
"""Module that retrieves the top ten hot posts from a subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {
        "User-Agent": "Python:alu-reddit-api:v1.0 (by /u/your_username)"
    }

    response = requests.get(
        url,
        headers=headers,
        params={"limit": 10},
        allow_redirects=False
    )
