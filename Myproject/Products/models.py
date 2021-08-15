from django.db import models
from django.db.models.base import Model
class Products(models.Model):
    name=models.CharField(max_length=20)
    weight=models.CharField(max_length=10)
    price=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

# Create your models here.
# from django.db import models

# from django.contrib.auth.models import User  

# class User(models.Model):
#     first_name=models.CharField(max_length=10)
#     last_name=models.CharField(max_length=10)
#     email=models.EmailField()
#     password=models.CharField(max_length=20)
#     username=models.CharField(max_length=10)

# class Post(models.Model):
#     user=models.ForeignKey(User, on_delete=models.CASCADE)
#     text=models.CharField(max_length=100)
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)