#!/usr/bin/python3
""" Gather data from an API  """

if __name__ == "__main__":
    import csv
    from requests import get
    from sys import argv, exit
    import sys

    try:
        employ_id = argv[1]
        is_int = int(employ_id)
    except ValueError:
        exit()
# retrieves the value of cmdline arg,converts it to int, if any error, it exits

    url_user = "https://jsonplaceholder.typicode.com/users?id=" + employ_id
    url_todo = "https://jsonplaceholder.typicode.com/todos?userId=" + employ_id
# amends the api url to get the user info & the associated todo info

    r_user = get(url_user)
    r_todo = get(url_todo)
# uses get fxn to make requests to the constructed urls, store in a variable

    try:
        js_user = r_user.json()
        js_todo = r_todo.json()

    except ValueError:
        print("Not a valid JSON")

    data = [["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]]

    for user in js_user:
        USER_ID = employ_id
        USERNAME = user.get('username')

        for todo in js_todo:
            TASK_TITLE = todo.get('title')
            TASK_COMPLETED_STATUS = todo.get("completed")

            TASK_COMPLETED_STATUS = (str(TASK_COMPLETED_STATUS)
                                    .lower() == 'true')

            data.append([USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])

    csv_file_name = f"{USER_ID}.csv"

    with open(csv_file_name, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=',',
            quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerows(data[1:])
