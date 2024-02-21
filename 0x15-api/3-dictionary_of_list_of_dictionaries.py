#!/usr/bin/python3
""" Gather data from an API  """

if __name__ == "__main__":
    from requests import get
    from sys import argv, exit
    import json

    url_user = "https://jsonplaceholder.typicode.com/users"
    url_todo = "https://jsonplaceholder.typicode.com/todos"
# amends the api url to get the user info & the associated todo info

    r_user = get(url_user)
    r_todo = get(url_todo)
# uses get fxn to make requests to the constructed urls, store in a variable
# data received from get is in json format, we use
# .json() from request module t parse it to a string

    try:
        js_user = r_user.json()
        js_todo = r_todo.json()

    except ValueError:
        print("Not a valid JSON")

    if js_user and js_todo:
        data = {}
        user_names = {}
        for user in js_user:
            USER_ID = user.get('id')
            USERNAME = user.get('username')
            data[USER_ID] = []
            user_names[USER_ID] = USERNAME

        for todo in js_todo:
            TASK_COMPLETED_STATUS = todo.get("completed")
            TASK_TITLE = todo.get('title')
            user_id = todo.get("userId")

            dic = {"task": TASK_TITLE,
                   "completed": TASK_COMPLETED_STATUS,
                   "username": user_names.get(user_id)}

            if data.get(user_id) is not None:
                data.get(user_id).append(dic)

            with open('todo_all_employees.json', 'w', newline='') as jsonfile:
                json.dump(data, jsonfile)
# with open(json_file_path, 'w') as json_file: is the syntax
# todo_all_employees + '.json represents json_file_path
# id holds the value passed as cmdline arg, .json is appended to it
