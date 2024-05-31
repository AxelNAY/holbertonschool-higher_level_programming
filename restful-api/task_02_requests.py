#!/usr/bin/python3
import json
import csv
import request

response = requests.get('https://jsonplaceholder.typicode.com/posts')


def fetch_and_print_posts():
    """Fetches all post from JSONPlaceholder"""
    print(f'Status Code: {response.status_code}')

    if reponse.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """fetches all post from JSONPlaceholder."""
    if reponse.status_code == 200:
        posts = response.json()
        data = [{'id': post['id'], 'title': post['title'],
                 'body': post['body']} for post in posts]

        with open('posts.csv', 'w', newline='') as file_csv:
            key = ['id', 'title', 'body']
            csvWriter = csv.DictWriter(file_csv, key)
            csvWriter.writeheader()
            csvWriter.writerows(data)
