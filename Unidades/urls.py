from django.conf.urls import url

from Unidades.views import *

urlpatterns = [
    url(r'^unidades/', UnidadesList.as_view(), name='Unidades')
]