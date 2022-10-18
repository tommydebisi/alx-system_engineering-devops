#!/usr/bin/python3
"""
    Api usage and exporting to json
"""
import json
import requests
from sys import argv, exit


if __name__ == "__main__":
    try:
        if len(argv) < 2 or type(eval(argv[1])) is not int:
            exit(1)

        url = 'https://jsonplaceholder.typicode.com'
        u_id = argv[1]
        new_dict = dict()

        todo_url = '{}/users/{}/todos'.format(url, u_id)
        user_url = '{}/users/{}'.format(url, u_id)
        # get user's name
        user = requests.get(user_url)
        user_name = user.json().get('username')

        # get tasks done by user
        todo = requests.get(todo_url)
        tasks = todo.json()
        new_dict['{}'.format(u_id)] = []
        for task in tasks:
            new_dict.get('{}'.format(u_id)).append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user_name
            })

        with open('{}.json'.format(u_id), 'x', encoding='utf-8') as f:
            json.dump(new_dict, f)
    except Exception:
        exit(1)
