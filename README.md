## Todo App
This is a Flask REST API for a todo application


### Prerequisites
This assumes you have the following installed locally:
1. Python 3 and higher
2. Postgres

### Getting started
1. Clone this repository:

```bash
$ git clone <repo>
```

2. Create a virtual environment and install all requirements:

```bash
$ python3 -m venv venv && source venv/Scripts/activate && pip3 install -r requirements.txt
```
3. Create a .env file at the root of the directory using the variables in sample.env file at the root of the project directory.

```bash
$ cp sample.env .env
```
4. Run migrations:

```bash
$ python manage.py db init && python manage.py db migrate
```

5. Run your server:

```
$ python manage.py runserver
```