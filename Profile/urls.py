from django.conf.urls import url

from Profile.views import *

urlpatterns = [
    url(r'^profile/', ProfileList.as_view(), name='Profile')
]