from django.urls import path

from .views import *

urlpatterns = [
  path('', index),
  path('<int:id>', getGroupById),
  path('<int:gid>/user/<int:zid>/permission', getPermission, name="getPermission"),
  path('<int:gid>/photo/<str:photo>', addPhoto),
  path('<int:gid>/description/<str:descrip>', addDes),
  path('<int:gid>/calendar', addCalendar),
  path('<int:gid>/delete', deleteGroup)
]