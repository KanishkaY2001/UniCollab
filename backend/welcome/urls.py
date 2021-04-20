from django.urls import path

from .views import *

urlpatterns = [
  path('register/<str:name>/<str:email>/<str:password>', register),
  path('login/<str:email>/<str:password>', login)
]