#!/usr/bin/python3
"""Return information about an employee's TODO list given their id
   And export data in the json format
"""
import json
import requests
import sys
if __name__ == "__main__":
    user_id = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(user_url)
    user = response.json()
    username = user.get('username')

    todos_url = f"{user_url}/todos"
    response = requests.get(todos_url)
    tasks = response.json()

    data = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in tasks
        ]
    }
    filename = f"{user_id}.json"
    with open(filename, 'w') as f:
        json.dump(data, f)
