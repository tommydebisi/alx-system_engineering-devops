#!/usr/bin/python3
"""
    Api usage and exporting to all tasks to json
"""
import json
import requests
from sys import exit


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    n_users = len(requests.get('{}/users'.format(url)).json())
    u_id = 1
    new_dict = dict()
    while u_id <= n_users:

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
                "username": user_name,
                "task": task.get('title'),
                "completed": task.get('completed')
            })
        u_id += 1

    with open('todo_all_employees.json', 'x', encoding='utf-8') as f:
        json.dump(new_dict, f)
