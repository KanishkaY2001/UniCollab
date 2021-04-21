from django.urls import path

from .views import *
from groups.views import getGroupByRoom

urlpatterns = [
  path('', index),
  path('<int:id>', getRoomById),
  path('<int:rid>/groups', getGroupByRoom),
  path('<int:id>/<int:rid>/creategroup/<str:name>', createGroup)
]
