from django.contrib import admin
from .models import  Mypost
# from django.contrib.auth.models import User
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display=['first_name', 'last_name','email', 'username']

@admin.register(Mypost)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','user','text','created_at','updated_at']

# Register your models here.
