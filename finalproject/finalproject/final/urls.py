from django.urls import path
from . import views

urlpatterns = [
    path('',views.first,name='first'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('register',views.register,name='register'),
    # path('new',views.new,name='new'),
    path('confirm',views.confirm,name='confirm'),
    path('new', views.new, name='new'),
]
