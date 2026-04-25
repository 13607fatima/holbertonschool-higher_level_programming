#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    headers = {'cfclearance': 'true'}
    r = requests.get(url, headers=headers)
    x_request_id = r.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
