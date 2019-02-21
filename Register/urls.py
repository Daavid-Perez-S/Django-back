from django.conf.urls import url

from Register.views import *

urlpatterns = [
    url(r'^register/', RegisterList.as_view(), name='Register')
]