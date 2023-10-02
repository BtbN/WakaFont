#!/usr/bin/env python3
import requests
import json
import sys

def wk_api_req(ep, full=True, data=None, put=False):
    WK_API_BASE="https://api.wanikani.com/v2"

    headers = {
        "Authorization": "Bearer " + sys.argv[1],
        "Wanikani-Revision": "20170710"
    }

    if data is not None:
        if put:
            res = requests.put(f"{WK_API_BASE}/{ep}", headers=headers, json=data)
        else:
            res = requests.post(f"{WK_API_BASE}/{ep}", headers=headers, json=data)
    else:
        res = requests.get(f"{WK_API_BASE}/{ep}", headers=headers)
    res.raise_for_status()
    data = res.json()

    if full and "object" in data and data["object"] == "collection":
        next_url = data["pages"]["next_url"]
        while next_url:
            res = requests.get(next_url, headers=headers)
            res.raise_for_status()
            new_data = res.json()

            data["data"] += new_data["data"]
            next_url = new_data["pages"]["next_url"]

    return data

if len(sys.argv) != 2:
    print("Invalid args. Pass WK API Key.")
    sys.exit(2)

data = wk_api_req("subjects?types=radical&hidden=false")

for subj in data["data"]:
    if subj["object"] == "radical" and not subj["data"]["characters"]:
        for img in subj["data"]["character_images"]:
            if img["content_type"] == "image/svg+xml":
                req = requests.get(img['url'])
                req.raise_for_status()
                with open("svg/" + subj["data"]["slug"] + ".svg", "w") as f:
                    f.write(req.text)
                break
