#!/usr/bin/python3

from pathlib import Path
import json
import os
import sys

try:
    from github import Github, GithubException
except ImportError:
    sys.exit("Please install pygithub package via pip")

home = str(Path.home())
token = str(open(home + "/.githubtoken", "r").read().strip())
g = Github(token)

ANDROID_BUILD_TOP = os.getenv("ANDROID_BUILD_TOP")

try:
    zip = os.path.abspath(sys.argv[1])
    zipName = zip.split("/")[-1]
except IndexError:
    sys.exit("Incorrect file!")

if "Streak" not in zip and ".zip" not in zip:
    sys.exit("Incorrect file!")

codename = zipName.split("-")[4]
date = (zipName.split("-")[5] + "-" + zipName.split("-")[6]).split(".")[0]
variant = zipName.split("-")[3]

print("Releasing " + variant + " build for " + codename)

repos = g.get_organization("ProjectStreak-Devices").get_repos()
for r in repos:
    if codename in r.name and "device_" in r.name:
        repo = r
        print("Repo found for your device: " + repo.name)

if not repo:
    sys.exit("\nERROR: Can't find repo for " + codename) 

tag = date + "-" + variant
title = "Streak-" + tag

try:
    release = repo.create_git_release(tag, title, "Automated release of " + zipName)
    print("Uploading asset...")
    release.upload_asset(zip)
    print("Asset uploaded!")
except GithubException:
    sys.exit("Release already exists!")

datetime = int(open(ANDROID_BUILD_TOP + "/out/build_date.txt", "r").read())
url = "https://github.com/ProjectStreak-Devices/" + repo.name + "/releases/download/" + tag + "/" + zipName
checksum = open(zip + ".sha256sum", "r").read().split(" ")[0]
filesize = os.path.getsize(zip)
version = zipName.split("-")[1]

template = {
  "response": [
    {
      "datetime": datetime,
      "filename": zipName,
      "id": checksum,
      "romtype": variant,
      "size": filesize,
      "url": url,
      "version": version
    }
  ]
}

jsonFile = open(ANDROID_BUILD_TOP + "/streak_ota/devices/" + codename + "/" + variant.lower() + ".json", "w")
jsonFile.write(json.dumps(template, indent=2))
jsonFile.close()

print("Release created: " + title + "!")
print("Don't forget to commit and push streak_ota repository!")
