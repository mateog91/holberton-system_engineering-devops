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
from calendar import c
from email.quoprimime import quote


if __name__ == "__main__":
    import csv
    import requests
    import sys
    # capture user id from input arguments
    user_id = sys.argv[1]
    # user_id = 2

    # define url
    url = 'https://jsonplaceholder.typicode.com'
    # fetch user dictionary
    user_d = requests.get('{}/users/{}'.format(url, user_id)).json()
    # fetch list of tasks according to userid
    user_tasks_l = requests.get(
        '{}/todos?userId={}'.format(url, user_id)).json()

    total_tasks = len(user_tasks_l)
    # extract title of tasks that have been completed
    task_titles_completed = [task.get('title')
                             for task in user_tasks_l if task.get('completed')]

    total_completed = len(task_titles_completed)
    name = user_d.get('name')

    # CSV TASK
    filename = "{}.csv".format(user_id)

    rows = [
        [user_id, name, task.get('completed'), task.get('title')]
        for task in user_tasks_l
    ]

    # writing to csv file
    with open(filename, 'w', newline="") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile, quotechar='"',
                               quoting=csv.QUOTE_ALL, delimiter=",")

        # writing the data rows
        csvwriter.writerows(rows)
