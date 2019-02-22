USER="david"
PASS="pesddya97"
MAIL="playeando.97@gmail.com"
script="
from django.contrib.auth.models import User;

username = '$USER';
password = '$PASS';
email = '$MAIL';

if User.objects.filter(username=username).count()==0:
    User.objects.create_superuser(username, email, password);
    print('Cuenta superusuario creado.');
else:
    print('Creacion de cuenta de superusuario saltada.');
"
printf "$script" | python manage.py shell
