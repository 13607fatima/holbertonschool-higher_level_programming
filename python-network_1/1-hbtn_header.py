#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    headers = {'cfclearance': 'true'}
    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:
        headers_dict = dict(response.info())
        print(headers_dict.get('X-Request-Id'))
