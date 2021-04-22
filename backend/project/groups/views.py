from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime
import json

from .models.groups import Group
# from students.models import Student
from groups.models.groupMembers import GroupMember
from groups.models.groupCalendars import Calendar
from rooms.models import Room

from students.serializers import StudentSerializer
from groups.serializers import CalendarSerializer

# Create your views here.
def getGroupById(request, id=id):
  result = {}
  for group in Group.objects.all():
    if group.id == id:
      result = getGroupJson(group)
      break
  return JsonResponse(result, safe=False)

def index(request, id=id):
  groups = []
  for group in Group.objects.all():
      # 2019-01-07 10:00
      # startTime = group.preferredmeetingStartTime.strftime("%Y-%m-%d %H:%M")
      # endTime = group.preferredmeetingEndTime.strftime("%Y-%m-%d %H:%M")
      groups.append(getGroupJson(group))
  return JsonResponse(groups, safe=False)

def getPermission(request, gid, zid):
  result = {
    'inGroup': False,
    'isMember': False,
    'isOwner': False
  }
  for group in Group.objects.all():
    print("here")
    if (group.id == gid and group.owner.id == zid):
      result = {
        'inGroup': True,
        'isMember': True,
        'isOwner': True
      }
    return JsonResponse(result, safe=False)

  for groupMem in GroupMember.objects.all():
    if (groupMem.group.id == gid and groupMem.member.id == zid):
      if groupMem.status == True:
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
  return JsonResponse(result, safe=False)

def getGroupByRoom(request, rid):
  groups = []
  for group in Group.objects.all():
    if group.room.id == rid:
      groups.append(getGroupJson(group))

  return JsonResponse(groups, safe=False)

def getGroupJson(group):
    photo = json.dumps(str(group.photo))
    # 2019-01-07 10:00
    # startTime = group.preferredmeetingStartTime.strftime("%Y-%m-%d %H:%M")
    # endTime = group.preferredmeetingEndTime.strftime("%Y-%m-%d %H:%M")
    id = group.id
    members = []
    members.append(StudentSerializer(group.owner).data)
    members = getMember(id, members)
    print(members)
    skills = getSkills(id)
    vacancy = group.capacity - len(members) - 1
    events = getCalendar(id)
    result = {
      'name': group.name, 
      'room': group.room.name,
      'owner': StudentSerializer(group.owner).data,
      'members': members,
      'descript': group.description,
      'preferLoc': group.preferredmeetingLoc,
      # 'preferredmeetingStartTime': startTime,
      # 'preferredmeetingEndTime': endTime,
      'photo': photo,
      'skills': skills,
      'capacity': group.capacity,
      'vacancy': vacancy,
      'events': events
    }

    return result

def getMember(id, members):
  for groupMem in GroupMember.objects.all():
    if (groupMem.group.id == id and groupMem.status):
      info = StudentSerializer(groupMem.member).data
      members.append(info)
  return members
 
# def getSkills(id):
#   skills = []
#   for gk in GroupSkill.objects.all():
#     if(gk.group.id == id):
#       skills.append(gk.skill.name)
#   return skills

def getCalendar(id):
  events = []
  for event in Calendar.objects.all():
    if event.group.id == id:
      events.append(CalendarSerializer(event).data)
  return events