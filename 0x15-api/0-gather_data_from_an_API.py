#!/usr/bin/python3
"""Pulls the necessary data... and thank you for reading this"""
from sys import argv
from requests import get
id, req = int(argv[1]), "https://jsonplaceholder.typicode.com"


def name():
    """Fetches the employee name from the JSON API"""
    user_data = get(req + '/users').json()
    for data in user_data:
        if data['id'] == id:
            specific_employee = data
            return specific_employee['name']

def comp_tasks():
    """Fetches the number of tasks the specific employee has completed"""
    task_data = get(req + '/todos').json()
    completed_tasks = 0
    for data in task_data:
        if data['userId'] == id and data['completed'] == True:
                completed_tasks += 1
    return completed_tasks

def total_tasks():
    """Fetches the total number of tasks assigned to a specific employee"""
    task_data = get(req + '/todos').json()
    total_tasks = 0
    for data in task_data:
        if data['userId'] == id:
                total_tasks += 1
    return total_tasks

def comp():
    """Fetches the tasks the specific employee has completed"""
    task_data = get(req + '/todos').json()
    completed_tasks = []
    for data in task_data:
        if data['userId'] == id and data['completed'] == True:
                completed_tasks.append(data['title'])
    return completed_tasks

if __name__ == "__main__":
    name, comp, total, task_list = name(), comp_tasks(), total_tasks(), comp()
    print("Employee {} is done with tasks({}/{}):".format(name, comp, total))
    for tasks in task_list:
        print('\t {}'.format(tasks))
