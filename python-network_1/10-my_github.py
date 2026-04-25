#!/usr/bin/python3
"""
Takes GitHub credentials and uses the GitHub API to display the user id.
Usage: ./10-my_github.py <username> <personal_access_token>
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    headers = {'cfclearance': 'true'}
    auth = (username, token)
    r = requests.get(url, auth=auth, headers=headers)
    try:
        json_data = r.json()
        print(json_data.get('id'))
    except ValueError:
        print("None")
