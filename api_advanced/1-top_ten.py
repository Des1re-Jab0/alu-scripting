#!/usr/bin/python3
"""Recursively collect all hot post titles of a subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return a list of all hot post titles, or None if the subreddit is invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})

    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))

    after = data.get("after")
    if after is not None:              # there's another page, go get it
        return recurse(subreddit, hot_list, after)

    return hot_list                    # no more pages, we're done

