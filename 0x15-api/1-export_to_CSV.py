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
    except Exception:
        exit(1)

    count = 1
    u_id = argv[1]

    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        u_id
    )
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        u_id
    )
    # get user's name
    user = requests.get(user_url)
    user_name = user.json().get('name')

    # get tasks done by user
    todo = requests.get(todo_url)
    with open('{}.csv'.format(u_id), 'w', encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        new_list = list()
        for attr in todo.json():
            new_list.append(u_id)
            new_list.append(user_name)
            new_list.append(attr.get('completed'))
            new_list.append(attr.get('title'))
            writer.writerow(new_list)
            new_list.clear()
