#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the body
of the response. If the status code is >= 400, prints the error code.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    headers = {'cfclearance': 'true'}
    r = requests.get(url, headers=headers)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
