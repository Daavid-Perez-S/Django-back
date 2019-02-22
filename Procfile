release: python manage.py makemigrations
release: python manage.py migrate
release: chmod u+x release.sh && ./release.sh
web: gunicorn back.wsgi --log-file -
