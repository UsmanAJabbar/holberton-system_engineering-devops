#!/usr/bin/python3
"""Pulls the necessary data... and thank you for reading this"""
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    id, req = int(argv[1]), "https://jsonplaceholder.typicode.com"

    task_data = get(req + '/todos').json()
    user_data = get(req + '/users').json()
    for data in user_data:
        if data['id'] == id:
            name = data.get('username')

    the_dayta = {id: [{'task': task.get('title'),
                       'completed': task.get('completed'),
                       'username': name} for task in task_data]}

    filename = '{}.json'.format(id)
    with open(filename, mode='w') as the_file:
        json.dump(the_dayta, the_file)
