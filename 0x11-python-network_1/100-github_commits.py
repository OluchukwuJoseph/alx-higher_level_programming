#!/usr/bin/python3
"""
    This script list 10 commits (from the most recent to oldest)
    of the repository passed
"""
import requests
import sys


if __name__ == '__main__':
    REPO_NAME = sys.argv[1]
    OWNER = sys.argv[2]
    URL = f'https://api.github.com/repos/{OWNER}/{REPO_NAME}/commits'

    response = requests.get(URL)

    if response.status_code == 200:
        commits = response.json()

        for count, commit in enumerate(commits):
            if count > 9:
                break
            print(f"{commit.get('sha')}: {commit['commit']['author']['name']}")
