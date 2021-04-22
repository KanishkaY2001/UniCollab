from django.contrib import admin

from .models.groups import Group 
from .models.groupCalendars import Calendar 
from .models.groupMembers import GroupMember

# Register your models here.

admin.site.register(Group)
admin.site.register(Calendar)
admin.site.register(GroupMember)

