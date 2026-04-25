#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter 'q'.
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    payload = {'q': q}
    headers = {'cfclearance': 'true'}
    try:
        r = requests.post(url, data=payload, headers=headers)
        json_data = r.json()
        if not json_data:
            print("No result")
        else:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
    except ValueError:
        print("Not a valid JSON")
