#!/usr/bin/python3
"""
    This script takes your GitHub credentials and
    uses the GitHub API to display your id
"""
import requests
import sys


if __name__ == '__main__':
    USER_NAME = sys.argv[1]
    GITHUB_PAT = sys.argv[2]

    headers = {'accept': 'application/vnd.github+json',
               'Authorization': f'Bearer {GITHUB_PAT}',
               'X-GitHub-Api-Version': '2022-11-28'}

    response = requests.get(f'https://api.github.com/users/{USER_NAME}',
                            headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        print(user_data['id'])
    else:
        print('None')
