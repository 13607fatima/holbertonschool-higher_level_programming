#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using the requests package.
"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    headers = {'cfclearance': 'true'}
    r = requests.get(url, headers=headers)
    body = r.text

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
