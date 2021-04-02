from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from . import forms


# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# from django.contrib.auth import login, authenticate
# from django.views.generic import CreateView
# from django.shortcuts import render, redirect

def index(request):
    # return HttpResponse("hello world!")
    posts = Post.objects.order_by('-published')
    return render(request, 'posts/post.html', {'posts':posts})

def geo_index(request):
    return render(request, "posts/geo_index.html")
# Create your views here.

def post_detail(request,post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post_detail.html',{'post':post})

#login機能実装
class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "posts/login.html"

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "posts/logout.html"

class IndexView(TemplateView):
    template_name = "posts/index.html"

class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "posts/register.html"
    success_url = reverse_lazy("login")
    
#フォロー機能実装

