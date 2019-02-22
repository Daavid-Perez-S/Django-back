release: python manage.py makemigrations
release: python manage.py migrate
release: ./release-tasks.sh
web: gunicorn back.wsgi --log-file -
