#!/usr/bin/python3

import requests
import sys

def get_employee_todo_list(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        if user_response.status_code == 200 and todos_response.status_code == 200:
            user_data = user_response.json()
            todos_data = todos_response.json()

            completed_tasks = [task for task in todos_data if task["completed"]]
            total_tasks = len(todos_data)
            completed_count = len(completed_tasks)

            print(f"Employee {user_data['name']} is done with tasks({completed_count}/{total_tasks}):")

            for task in completed_tasks:
                print(f"    {task['title']}")

        else:
            print("Error: Unable to fetch data. Please check the employee ID.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    if not employee_id.isdigit():
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_list(int(employee_id))
