#!/usr/bin/python3
"""Return information about all employee's TODO lists
   And export data in the json format
"""
import json
import requests
if __name__ == "__main__":
    data = {}
    users_url = f"https://jsonplaceholder.typicode.com/users"
    users = requests.get(users_url).json()

    for user in users:
        username = user.get('username')
        user_id = user.get('id')
        todos_url = f"{users_url}/{user_id}/todos"
        tasks = requests.get(todos_url).json()

        data[user_id] = [
                            {
                                "task": task.get("title"),
                                "completed": task.get("completed"),
                                "username": username
                            }
                            for task in tasks
                        ]
    filename = "todo_all_employees.json"
    with open(filename, 'w') as f:
        json.dump(data, f)
