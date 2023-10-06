from django.urls import path
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("test/", Test, name="Test"),
   
]