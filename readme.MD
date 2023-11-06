# DJango-example

Django example project to practice serializer and scrapping.

The Project includes single app:

- CourseApi: Crud App For course entity. Also includes scrapping data from a custom url [Link](https://sysrev.cs.binghamton.edu/)

### How to Run:

- Clone this project
- Load libraries:
  ```
  pipenv install
  ```
- To add a package
  ```
  pipenv install <package>
  ```
- Create and activate environment:
  ```
  pipenv shell
  ```
- Run Migrations:
  ```
  python manage.py migrate
  ```
- Run server:
  ```
  python manage.py runserver
  ```
