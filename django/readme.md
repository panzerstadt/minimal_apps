Django from scratch (for pushing to heroku)

1. pip install pipenv
2. make folder
3. pipenv install
4. pipenv shell
5. pip install django
6. django-admin startproject mynewproject
7. cd mynewproject
8. django-admin startapp mynewapp
9. check with either 'python manage.py runserver' or 'heroku local'
10. if using 'heroku local', make sure you have a Procfile to tell heroku what to do
