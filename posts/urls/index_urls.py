from django.conf.urls import url
from .. import views

urlpatterns = [
        url(r'^$', views.index, name = 'post'), #views.py の index 関数に行け
    ]