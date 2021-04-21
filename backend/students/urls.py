from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('<int:id>', user),
    path('<int:id>/allrooms', getRoomsNotIn),
    path('<int:id>/rooms', studentRooms),
    path('<int:id>/groups', studentGroups),
    path('<int:id>/joinroom/<int:rid>', joinRoom),
    path('register/<str:name>/<str:email>/<str:password>', register),
    path('login/<str:email>/<str:password>', login),
    path('<int:id>/addcourse/<str:cname>', addCourse),
    path('<int:id>/removecourse/<str:cname>', deleteCourse),
    path('<int:id>/location/<str:loc>', addLocation),
    path('<int:id>/sync', syncCalendar),
    path('<int:id>/leaveroom/<int:rid>', leaveRoom),
    path('<int:id>/getcalendar', getStudentCalendar),
    path('<int:id>/deletecalendar', deleteCalendar)
]