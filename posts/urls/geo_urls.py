from django.conf.urls import url
from .. import views

urlpatterns = [
        url(r'^', views.geo_index, name = 'geo_index')
    ]