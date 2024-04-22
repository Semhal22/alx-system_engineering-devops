#!/usr/bin/python3
"""Return information about an employee's TODO list given their id"""
import requests
import sys
if __name__ == "__main__":
    completed = 0
    employee_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(user_url)
    user = response.json()
    name = user.get('name')

    todos_url = f"{user_url}/todos"
    response = requests.get(todos_url)
    tasks = response.json()

    for task in tasks:
        if task.get('completed'):
            completed += 1
    total = len(tasks)
    print(f"Employee {name} is done with tasks({completed}/{total}):")
    for task in tasks:
        if task.get('completed'):
            print(f"\t {task.get('title')}")
