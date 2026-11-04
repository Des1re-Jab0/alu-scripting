#!/usr/bin/python3

import requests


def top_ten(subreddit):

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting/1.0"}
    params = { "limit" : 10}


    response = requests.get(url, headers=headers ,params=params, allow_redirect=false)


    if response.status_code != 200:
        print (none)
        return 


    posts = response.json().get("data",{}).get("children",[])
    for post in posts:
        print (post.get("data",{}).get("title"))

