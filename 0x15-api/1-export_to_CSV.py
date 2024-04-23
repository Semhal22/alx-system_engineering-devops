#!/usr/bin/python3
"""Return information about an employee's TODO list given their id
   And export data in the CSV format
"""
import csv
import requests
import sys
if __name__ == "__main__":
    completed = 0
    csv_rows = []
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
    for task in tasks:
        title = task.get('title')
        task_completed = task.get('completed')
        csv_rows.append([employee_id, name, task_completed, title])

    filename = f"{employee_id}.csv"
    with open(filename, 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows(csv_rows)
