release: python manage.py makemigrations
release: python manage.py migrate
release: chmod u+x release-tasks.sh && ./release-tasks.sh
web: gunicorn back.wsgi --log-file -
