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
    import requests
    import sys
    # capture user id from input arguments
    user_id = sys.argv[1]

    # define url
    url = 'https://jsonplaceholder.typicode.com'
    # fetch user dictionary
    user_d = requests.get('{}/users/{}'.format(url, user_id)).json()
    # fetch list of tasks according to userid
    user_tasks_l = requests.get(
        '{}/todos?userId={}'.format(url, user_id)).json()

    total_tasks = len(user_tasks_l)
    # extract title of tasks that have been completed
    task_titles = [task.get('title')
                   for task in user_tasks_l if task.get('completed')]

    total_completed = len(task_titles)
    name = user_d.get('name')

    # print name and tasks done/total tasks
    print(
        "Employee {} is done with tasks({}/{}):".format(name, total_completed,
                                                        total_tasks))
    # print iteratively titles of completed tasks using list comprehension
    [print("\t {}".format(title)) for title in task_titles]
