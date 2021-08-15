from django.urls import path
from . import views
urlpatterns=[path('', views.register, name='signin'),
path('login', views.loginuser, name='login'),
path('logout',views.logoutuser, name="logout"),
path('post', views.post, name='post'),
path('update/<int:pk>', views.upd, name='update'),
path('delete/<int:pk>', views.delt, name='del'),

] 