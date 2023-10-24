#!/usr/bin/python3

'''
Export data in the JSON format
'''

import json
import requests
from sys import argv


def getAll():
    ''' Records all tasks from all employees '''
    URL = 'https://jsonplaceholder.typicode.com/'
    USERS = requests.get(URL + 'users').json()
    TASKS = requests.get(URL + 'todos').json()
    _allData = {}
    for user in USERS:
        _users = []
        for task in TASKS:
            if user['id'] == task['userId']:
                userData = {}
                userData['task'] = task['title']
                userData['completed'] = task['completed']
                userData['username'] = user['username']
                _users.append(userData)
        _allData[user['id']] = _users
    with open('todo_all_employees.json', 'w') as f:
        json.dump(_allData, f)


if __name__ == '__main__':
    getAll()
