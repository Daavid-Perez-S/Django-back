from django.conf.urls import url

from Gps.views import *

urlpatterns = [
    url(r'^gps/', GpsList.as_view(), name='Gps')
]