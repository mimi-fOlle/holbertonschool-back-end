#!/usr/bin/python3
"""Returns info about his/her TODO list progress by giving employee ID"""
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    response1 = get('https://jsonplaceholder.typicode.com/todos/')
    data1 = response1.json()
    completed = 0
#    uncompleted = 0
    total = 0
    tasks = []
    response2 = get('https://jsonplaceholder.typicode.com/users/')
    data2 = response2.json()

    for i in data2:
        if i.get("id") == int(argv[1]):
            employee = i.get("name")

    for i in data1:
        if i.get("userId") == int(argv[1]):
            total += 1
            if i.get("completed") is True:
                completed += 1
                tasks.append(i.get("title"))
#            else:
#                uncompleted += 1
#        total = completed + uncompleted

    print("Employee {} is done with task({}/{}):".format(employee,
                                                         completed, total))

    for i in tasks:
        print("\t {}".format(i))
