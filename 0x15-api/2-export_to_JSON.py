#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
Requirements:
    You must use urllib or requests module
    The script must accept an integer as a parameter, which is the employee ID
    The script must display on the standard output the employee TODO
    list progress in this exact format:
        First line: Employee EMPLOYEE_NAME is done with tasks
        (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            EMPLOYEE_NAME: name of the employee
            NUMBER_OF_DONE_TASKS: number of completed tasks
            TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the
            sum of completed and non-completed tasks
        Second and N next lines display the title of completed tasks:
        TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""

if __name__ == "__main__":
    import json
    import requests
    import sys

    user_id = int(sys.argv[1])

    # define url
    url = 'https://jsonplaceholder.typicode.com'
    # fetch user dictionary
    user_d = requests.get('{}/users/{}'.format(url, user_id)).json()
    # fetch list of tasks according to userid
    user_tasks_l = requests.get(
        '{}/todos?userId={}'.format(url, user_id)).json()

    username = user_d.get('username')

    # CSV TASK
    filename = "{}.json".format(user_id)

    d = {user_id:
         [
             {"task": task.get('title'), "completed": task.get(
                 'completed'), "username": username}
             for task in user_tasks_l]
         }

    # writing to json file
    with open(filename, 'w') as jsonfile:
        json.dump(d, jsonfile)
