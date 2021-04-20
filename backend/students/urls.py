from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('<int:id>', user),
    path('<int:id>/rooms', studentRooms),
    path('<int:id>/groups', studentGroups),
    path('<int:id>/join/<int:rid>', joinRoom)
]