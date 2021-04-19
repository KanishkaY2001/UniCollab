from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import json

from .models import Group
# from students.models import Student
from groupMembers.models import GroupMember

from students.serializers import StudentSerializer

# Create your views here.
def getGroupById(request, id=id):
  result = {}
  for group in Group.objects.all():
    if group.id == id:
      photo = json.dumps(str(group.photo))
      print(group.photo)
      # 2019-01-07 10:00
      startTime = group.preferredmeetingStartTime.strftime("%Y-%m-%d %H:%M")
      endTime = group.preferredmeetingEndTime.strftime("%Y-%m-%d %H:%M")
      members = getMember(id)
      result = {
        'name': group.name, 
        'room': group.room.name,
        'owner': StudentSerializer(group.owner).data,
        'members': members,
        'descript': group.description,
        'preferLoc': group.preferredmeetingLoc,
        'preferredmeetingStartTime': startTime,
        'preferredmeetingEndTime': endTime,
        'photo': photo
      }
      break
  return JsonResponse(result, safe=False)

def index(request, id=id):
  groups = []
  for group in Group.objects.all():
      photo = json.dumps(str(group.photo.path))
      # 2019-01-07 10:00
      startTime = group.preferredmeetingStartTime.strftime("%Y-%m-%d %H:%M")
      endTime = group.preferredmeetingEndTime.strftime("%Y-%m-%d %H:%M")
      groups.append({
<<<<<<< HEAD
        'name': group.name
=======
        'name': group.name, 
        'room': group.room.name,
        'owner': group.owner.name,
        'descript': group.description,
        'preferLoc': group.preferredmeetingLoc,
        'preferredmeetingStartTime': startTime,
        'preferredmeetingEndTime': endTime,
        'photo': photo
>>>>>>> 20d6a42f81dc4aa409782823c05d06a7fccfbe06
      })
  return JsonResponse(groups, safe=False)

def getMember(id):
  members = []
  for groupMem in GroupMember.objects.all():
    if (groupMem.group.id == id and groupMem.status):
      info = StudentSerializer(groupMem.member).data
      members.append(info)
  return members

def getPermission(request, gid, zid):
  result = {
    'inGroup': False,
    'isMember': False,
    'isOwner': False
  }
  for groupMem in GroupMember.objects.all():
    if (groupMem.group.id == gid and groupMem.member.id == zid):
      if groupMem.group.status == True:
        result = {
          'inGroup': True,
          'isMember': False,
          'isOwner': False
        }
      else:
        result = {
          'inGroup': True,
          'isMember': False,
          'isOwner': False
        }
      break
    elif (groupMem.group.id == gid and groupMem.group.owner.id == zid):
      result = {
        'inGroup': True,
        'isMember': True,
        'isOwner': True
      }
      break
  return JsonResponse(result, safe=False)
  