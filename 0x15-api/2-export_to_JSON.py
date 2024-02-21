#!/usr/bin/python3
""" Gather data from an API  """

if __name__ == "__main__":
    from requests import get
    from sys import argv, exit
    import json

    try:
        id = argv[1]
        is_int = int(id)
    except ValueError:
        exit()
# retrieves the value of cmdline arg,converts it to int, if any error, it exits

    url_user = "https://jsonplaceholder.typicode.com/users?id=" + id
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId=" + id
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
        USER_ID = id
        USERNAME = js_user[0].get('username')

        js_list = []
        for todo in js_todo:
            TASK_COMPLETED_STATUS = todo.get("completed")
            TASK_TITLE = todo.get('title')

            dic = {"task": TASK_TITLE,
                   "completed": TASK_COMPLETED_STATUS,
                   "username": USERNAME}
            js_list.append(dic)

            data = {USER_ID: js_list}

            with open(id + '.json', 'w', newline='') as jsonfile:
                json.dump(data, jsonfile)
# with open(json_file_path, 'w') as json_file: is the syntax
# id + '.json represents json_file_path
# id holds the value passed as cmdline arg, .json is appended to it
# to form the path 2.json
