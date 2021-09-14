#!/usr/bin/python3
""" export data in the CSV format. """
import csv
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]

    user = requests.get(
       "https://jsonplaceholder.typicode.com/users/{}".format(user_id),
       verify=False).json()

    task = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            user_id), verify=False).json()

    with open("{}.csv".format(user_id), 'w', newline='') as csvfile:
        writer_t = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i in task:
            writer_t.writerow([int(user_id), user.get('username'),
                              i.get('completed'),
                              i.get('title')])
