#!/usr/bin/python3
"""
Fetches data from JSONPlaceholder API and processes it.
Includes printing titles and saving data to a CSV file.
"""
import csv
import requests


def fetch_and_print_posts():
    """Fetches all posts and prints their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Fetches all posts and saves id, title, and body to a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        processed_data = []

        for post in posts:
            post_dict = {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            }
            processed_data.append(post_dict)

        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(processed_data)


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
