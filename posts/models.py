from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.
# models.pyを編集した場合は毎回migrationが必要だよ→python manage.py makemigrations
# migrationが成功するとmigrationsファイルに00xx_xxxというファイルが増える
# そのファイルをいじって調整してからmigrate

#1:mの場合はforeignkey
# (models.Model)は継承している


class Post(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:30]
    
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    
class Testtable(models.Model):
    circlename = models.CharField(max_length=30)
    memberid = models.IntegerField()
    maketime = models.DateTimeField()
