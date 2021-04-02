from django.conf.urls import url
from .. import views

urlpatterns = [
    url(r'^login/', views.MyLoginView.as_view(), name="login"),
    url(r'^logout/', views.MyLogoutView.as_view(), name="logout"),
    url(r'^index/', views.IndexView.as_view(), name="index"),
    url(r'^register/', views.UserCreateView.as_view(), name="register"),
]