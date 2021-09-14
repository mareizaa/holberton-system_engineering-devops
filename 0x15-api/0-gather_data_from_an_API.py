#!/usr/bin/python3
"""Returns information about his/her TODO list progress"""
import requests
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(user_id))
    task = requests.get("https://jsonplaceholder.typicode.com/todos")

    complete = 0
    number_task = 0
    tasks = []

    for i in task.json():
        if i.get('userId') == int(user_id):
            if i.get('completed'):
                complete = complete + 1
                tasks.append('\t' + i.get('title'))
            number_task = number_task + 1

    user_name = user.json()['name']

    print("Employee {} is done with tasks({}/{})".format(user_name,
                                                         complete,
                                                         number_task))
    print("\n".join(tasks))
