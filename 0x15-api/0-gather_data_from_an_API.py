#!/usr/bin/python3
import requests
from sys import argv, exit


if __name__ == "__main__":
    try:
        if len(argv) < 2 or type(eval(argv[1])) is not int:
            exit(1)
    except Exception:
        exit(1)

    count = 1
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
        argv[1]
    )
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
        argv[1]
    )
    # get user's name
    user = requests.get(user_url)
    user_name = user.json().get('name')

    # get tasks done by user
    todo = requests.get(todo_url)
    task_len = len(todo.json())
    comp_task = sum([count for attr in todo.json()
                     if attr.get('completed') is True])

    print('Employee {} is done with tasks({}/{}):'.format(
        user_name, comp_task, task_len
    ))
    for attr in todo.json():
        if attr.get('completed') is True:
            print('\t{}'.format(attr.get('title')))
