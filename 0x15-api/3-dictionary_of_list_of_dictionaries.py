#!/usr/bin/python3
'''3-dictionary_of_list_of_dictionaries module'''
import json
import requests
import sys


if __name__ == '__main__':
    '''List of tasks'''
    todos = requests.get('https://jsonplaceholder.typicode.com/\
todos').json()
    employees = requests.get('https://jsonplaceholder.typicode.com/users'
                             ).json()
    '''Creating the subdictionaries, list and dictionary to export'''
    subdict = {}
    dict_list = []
    dict_export = {}
    '''Getting employee username'''
    for emp in employees:
        employee_username = emp.get('username')
        '''Making the export dictionary'''
        for todo in todos:
            if todo['userId'] == emp['id']:
                subdict['username'] = employee_username
                subdict['task'] = todo.get('title')
                subdict['completed'] = todo.get('completed')
                dict_list.append(subdict)
                subdict = {}
        dict_export[emp['id']] = dict_list
        dict_list = []
    '''Write to json file'''
    with open("todo_all_employees.json", "w") as f:
        json.dump(dict_export, f)
