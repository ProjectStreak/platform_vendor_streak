#!/usr/bin/python3

from github import Github, GithubException
from pathlib import Path
import json
import os
import requests
import sys

home = str(Path.home())
token = str(open(home + "/.githubtoken", "r").read().strip())
g = Github(token)

if sys.argv[1].find("https") != -1:
    print("URL detected, downloading...")
    zip_name = (sys.argv[1]).split("/")[-1]
    req = requests.get(sys.argv[1], allow_redirects=True)
    open(zip_name, "wb").write(req.content)
else:
    print("File detected...")
    zip_name = sys.argv[1]

codename = zip_name.split("-")[4]
date = zip_name.split("-")[5] + "-" + zip_name.split("-")[6]
date = date.split(".")[0]
variant = zip_name.split("-")[3]

print("Codename: " + codename)
print("Date: " + date)
print("Variant: " + variant)

devices_json = requests.get("https://raw.githubusercontent.com/ProjectStreak-Devices/official_devices/main/devices.json").text

brands_list = json.loads(devices_json)
brand = None
for fbrand in brands_list:
    for fcodename in brands_list[fbrand]:
        if fcodename == codename:
            brand = fbrand

if brand is None:
    sys.exit("\nERROR: Can't find repo for your device: " + codename)

repo = g.get_repo("ProjectStreak-Devices/device_" + brand + "_" + codename)
print("Repo found for your device: " + repo.name)

tag = date + "-" + variant
title = "Streak-" + tag

exp = input("Is this an experimental build? (Y/y) (Default: N) ")
if exp == "Y" or exp == "y":
    isExperimental = True
else:
    isExperimental = False

release = repo.create_git_release(tag, title, "Automated release of " + zip_name, prerelease=isExperimental)
print("Release created: " + str(release.title))
print("Uploading asset...")
release.upload_asset(zip_name)
print("Asset uploaded!")
