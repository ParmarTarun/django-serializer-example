# DJango-example

Django example project to practice serializer and scrapping.

The Project includes single app:

- CourseApi: Crud App For course entity. Also includes scrapping data from a custom url [Link](https://sysrev.cs.binghamton.edu/)

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
  python manage.py migrate
  ```
- Run server:
  ```
  python manage.py runserver
  ```
