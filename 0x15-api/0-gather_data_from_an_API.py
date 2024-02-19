#!/usr/bin/python3
""" Script that uses REST API and takes ID as arg to return TODO info """
from urllib imoport parse
import sys
from urllib.request import urlopen
import json
""" imports urllib.requests"""

if __name__ == "__main__":
    """ ensures that code will not run if imported """

        employee_id = int(sys.argv[1])
        
        url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
        with urlopen(url) as response:
            displayed_value = response.read()

            todo_item = json.loads(displayed_value)

        EMPLOYEE_NAME = todo_item[0]['username']
        TOTAL_NUMBER_OF_TASKS = len(todo_item)
        NUMBER_OF_DONE_TASKS = sum(1 for task in todo_list if task['completed'])

    print("Employee {} is done with tasks ({}/{})"
            .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS,TOTAL_NUMBER_OF_TASKS)
    print\t('TASK_TITLE')
    except:
        pass
