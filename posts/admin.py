from django.contrib import admin

# Register your models here.
from .models import Post
# from .models import InputForm

admin.site.register(Post)