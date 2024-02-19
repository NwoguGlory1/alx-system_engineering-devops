#!/usr/bin/python3
""" Script that uses REST API and takes ID as arg to return TODO info """
from urllib imoport parse
import sys
from urllib.request import urlopen
import json
""" imports urllib.requests"""

if __name__ == "__main__":
    """ ensures that code will not run if imported """
    try:
        int_value = sys.argv[1]
        url = 'https://jsonplaceholder.typicode.com/todos/1'
        with urlopen(url) as response:
            displayed_value = response.read()

        todo_item = json.loads.(displayed_value)
    a = 'Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):'
    print a
    print\t\s('TASK_TITLE')
    except:
        pass
