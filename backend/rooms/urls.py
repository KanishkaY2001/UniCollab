from django.urls import path

from .views import *
from groups.views import getGroupByRoom

urlpatterns = [
  path('', index),
  path('<int:id>', getRoomById),
  path('<int:rid>/groups', getGroupByRoom),
  path('<int:id>/<int:rid>/creategroup/<str:name>', createGroup),
  path('<int:id>/location/<int:rid>', getLocation),
  path('<int:id>/calendar/<int:rid>', getCalendarGroups),
  path('<int:id>/skills/<int:rid>', getSkillsGroups),
  path('<int:id>/<int:rid>/<int:gid>/members', getRoomMembers),
  path('<int:id>/overall/<int:rid>', getOverallGroups)
]
