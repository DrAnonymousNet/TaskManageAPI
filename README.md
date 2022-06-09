# Task State API


#  INSTALLATION

1. Clone the Repository

2. Ceate a virtual environment:

```
$ python3 -m venv venv
```

3. Activate Virtual Environment
```
$ source venv/bin/activate
```

4. Install the Required Packages

```
$ pip install -r requirements.txt
```

5. Change directory into the TaskManagerAPI/TaskManage

6. Run the development server

```
$ python manage.py runserver
```

# TEST 

> Test Cases in Task/test.py

To run Test:

```
python manage.py test
```

# ENDPOINT

API ENDPOINT'S


`GET    api/tasks/    Get all tasks`

`POST   api/tasks/     Create new Task`

`GET   api/tasks/<pk> Get a task`

`PUT   api/tasks/<pk> Update a task`

`DELETE  api/tasks/<pk> Delete a task`
