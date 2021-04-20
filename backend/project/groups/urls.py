from django.urls import path

from .views import *

urlpatterns = [
  path('', index),
  path('<int:id>', getGroupById),
  path('<int:gid>/user/<int:zid>/permission', getPermission, name="getPermission"),
]