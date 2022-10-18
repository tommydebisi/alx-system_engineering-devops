#!/usr/bin/python3
"""
    Api usage and exporting to csv
"""
import csv
import requests
from sys import argv, exit


if __name__ == "__main__":
    try:
        if len(argv) < 2 or type(eval(argv[1])) is not int:
            exit(1)

        count = 1
        u_id = argv[1]
        url = 'https://jsonplaceholder.typicode.com'

        todo_url = '{}/todos?userId={}'.format(url, u_id)
        user_url = '{}/users/{}'.format(url, u_id)
        # get user's name
        user = requests.get(user_url)
        user_name = user.json().get('name')

        # get tasks done by user
        todo = requests.get(todo_url)
        with open('{}.csv'.format(u_id), 'x', encoding="utf-8") as f:
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for attr in todo.json():
                writer.writerow([u_id, user_name, attr.get('completed'),
                                attr.get('title')])
    except Exception:
        exit(1)
