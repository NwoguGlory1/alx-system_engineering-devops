#!/usr/bin/python3
""" Script that uses REST API and takes ID as arg to return TODO info """

if __name__ == "__main__":
    """ ensures that code will not run if imported """
    import json
    import sys
    from urllib.request import urlopen
    """ imports several libraries"""

    try:
        if len(sys.argv) != 2:
            raise ValueError("Usage: python script.py <employee_id>")

        employe_id = int(sys.argv[1])

        url = f'https://jsonplaceholder.typicode.com/todos?userId={employe_id}'
        with urlopen(url) as response:
            body = response.read()
            todo_item = json.loads(body)

        EMPLOYEE_NAME = todo_item[0]['username']
        TOTAL_NUMBER_OF_TASKS = len(todo_item)
        NUMBER_OF_DONE_TASKS = sum(task['completed']
                for task in todo_item)

        print("Employee {} is done with tasks ({}/{}):".
            format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS)

        for task in todo_item:
        TASK_TITLE = task.get('title')
        if task.get('completed'):
            print("\t {}".format('TASK_TITLE')

    except Exception as e:
        pass
