from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('<int:id>', user),
    path('<int:id>/rooms', studentRooms),
    path('<int:id>/groups', studentGroups),
    path('<int:id>/joinroom/<int:rid>', joinRoom),
    path('register/<str:name>/<str:email>/<str:password>', register),
    path('login/<str:email>/<str:password>', login)
]