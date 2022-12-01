#!/usr/bin/python3
"""Returns info about his/her TODO list progress by giving employee ID"""
from sys import argv
import json
import requests


if __name__ == "__main__":
    response1 = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data1 = response1.json()
    completed = 0
    uncompleted = 0
    total = 0
    tasks = []
    response2 = requests.get('https://jsonplaceholder.typicode.com/users/')
    data2 = response2.json()

    for idx in data2:
        if idx.get("id") == int(argv[1]):
            employee = idx.get("name")

    for idx in data1:
        if idx.get("userId") == int(argv[1]):

            if idx.get("completed") is True:
                completed += 1
                tasks.append(idx.get("title"))
            else:
                uncompleted += 1
        total = completed + uncompleted

    print("Employee {} is done with task({}/{}):".format(employee,
                                                         completed, total))

    for idx in tasks:
        print("\t {}".format(idx))
