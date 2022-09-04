
from django.urls import path
from django.urls import re_path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),

]