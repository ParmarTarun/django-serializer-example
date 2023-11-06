# DJango-example

Django example project

A basic Django project to get started. Credits: [Real Python](https://realpython.com/get-started-with-django-1/)

The Project includes two apps:

- Pages: Basic App setup with a single template
- Parser: Crud App For course entity. Also includes scrapping data from a custom url [Link](https://sysrev.cs.binghamton.edu/)

### How to Run:

- Clone the repo
- Create and activate environment:
  - Linux/Mac:
    ```
    python -m venv env
    . env/bin/activate
    ```
- Load libraries:
  ```
  pip install -r requirements.txt
  ```
- Run Migrations:
  ```
  python manage.py migrate parser
  ```
- Run server:
  ```
  python manage.py runserver
  ```

### Usage:

- <b>pages/</b> : Html example page from templates
- <b>parser/</b>:
  - <b>dashboard/</b> : Dashboard for performing CRUD on Course
  - <b>courses/</b> : returns array of courses from database <br/>
    Following uses scrapping:
  - <b>courses/scrape</b> : returns array of all courses after scarpping from custom url
  - <b>courses/electives</b> : returns array of elective courses after scarpping from custom url
  - <b>courses/mandatory</b> : returns array of mandatory courses after scarpping from custom url
  - <b>courses/load</b> : populates db with data from scrapping
