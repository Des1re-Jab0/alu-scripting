#!/usr/bin/python3
"""Recursively count keywords in a subreddit's hot post titles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print how often each keyword appears across all hot post titles.

    Sorted by count (highest first); ties are broken alphabetically.
    Repeated keywords in word_list have their counts added together.
    """
    # First call only: start every unique keyword's tally at 0.
    if counts is None:
        counts = {}
        for word in word_list:
            counts[word.lower()] = 0

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0"}
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get("data", {})

    # Count keyword hits in each title on this page.
    for post in data.get("children", []):
        words = post.get("data", {}).get("title", "").lower().split()
        for key in counts:
            counts[key] += words.count(key)

    # Another page? Recurse to fetch it before printing anything.
    after = data.get("after")
    if after is not None:
        return count_words(subreddit, word_list, after, counts)

    # No more pages: add duplicate keywords together.
    totals = {}
    for word in word_list:
        key = word.lower()
        totals[key] = totals.get(key, 0) + counts[key]

    # Sort by count (descending), then alphabetically (ascending), skip zeros.
    for word, count in sorted(totals.items(), key=lambda p: (-p[1], p[0])):
        if count > 0:
            print("{}: {}".format(word, count))
