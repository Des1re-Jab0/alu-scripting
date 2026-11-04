#!/usr/bin/python3

import requests

def recurse(subreddit,hot_list=[], after=none):

    url= "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent":"alu-scripting/1.0"}
    params = {"limit":100,"after":after}

    response = request.get(url,headers=headers,params=params,allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get("data",{})

    for post in data .get("Children",[]):
        hot_list.append(post.get("data",{}).get("title"))

        after = data.get("after")
        if after is not None:
            return recurse(subreddit,hot_list,after)
        return hot_list
