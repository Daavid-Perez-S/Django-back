"""back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.conf.urls import url # Tutorial
from django.conf import settings # Tutorial
from django.contrib.auth.models import User
from rest_framework.authtoken import views # Tutorial
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)



# Estas son mis urls personales ***************

urlpatterns = [
    url(r'^api/v1/', include('Gps.urls')), # , namespace='Gps'  <-- Tuve que borrar esto porque me daba error
    url(r'^api/v1/', include('Profile.urls')),
    url(r'^api/v1/', include('Register.urls')),
    url(r'^api/v1/', include('Unidades.urls')),
    #url(r'^api/v1/auth', include('rest_framework.urls')), # , namespace='rest_framework'  <-- Tuve que borrar esto porque me daba error

    path('admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    re_path(r'^api/v1/login', include('Login.urls'))
]
