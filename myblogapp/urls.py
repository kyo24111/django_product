"""myblogapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings
from posts import views

urlpatterns = [
    url(r'^posts/', include('posts.urls.index_urls')), #何もなければ、posts/urls.pyに行け
    url(r'^posts/(?P<post_id>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^admin/', admin.site.urls),
    url(r'^geo/', include("posts.urls.geo_urls")),
    url(r'^accounts/', include("posts.urls.accounts_urls")),
    # url(r'^login/', include("posts.urls.login_urls")),
    # url(r'^register/', include("posts.urls.register_urls")),
    # url(r'^create/', include("posts.urls.accounts_urls")),
    # url(r'^login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='commons/login.html'), name='login'),
    # url(r'^logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    # url(r'^accounts/', include("django.contrib.auth.urls")),
    # url(r'^accounts/', include("posts.urls")),
    # url(r'^post_new_post', views.post_new_post),
    # url(r'^login', views.login_user),
    # url(r'^registration', views.registation_user),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
