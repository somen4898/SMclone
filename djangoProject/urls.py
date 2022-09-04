
from django.urls import re_path
from django.contrib import admin
from django.urls import path
from first_app import views
from django.conf.urls import include


urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    path('first_app/',include('first_app.urls')),
    path('admin/', admin.site.urls),


]


