from django.shortcuts import render
from django.http import JsonResponse

from .models import Student
from rooms.models import Room, Member
from groups.models.groups import Group
from groups.models.groupMembers import GroupMember
import json
# Create your views here.

def index(request):
    students = []
    for student in Student.objects.all():
        students.append({
            'name': student.name,
            'id': student.id,
        })
    return JsonResponse(students, safe=False)

def user(request, id=id):
    user = {}
    for student in Student.objects.all():
        if (student.id == id):
            user = {
                'name': student.name,
                'id': student.id,
            }
            break
    return JsonResponse(user, safe=False)

def studentRooms(request, id):
    rooms = []
    for memb in Member.objects.all():
        if (memb.student.id == zid): 
            rooms.append({
                "name": memb.room.name,
                "id": memb.room.id
            })
    return JsonResponse(rooms, safe=False)

def studentGroups(request, id):
    groups = []
    for grMemb in GroupMember.objects.all():
        photo = json.dumps(str(grMemb.group.photo))
        if (grMemb.member.id == zid):
            groups.append({
                "name": grMemb.group.name,
                "id": grMemb.group.id,
                "photo": grMemb.group.photo
            })
    return JsonResponse(groups, safe=False)

def joinRoom(request, id, rid):
    result = { "id" : rid }
    student = getStudent(id)
    for room in Room.objects.all():
        if (room.id == rid):
            room.members.add(student)
    return JsonResponse(result, safe=False)
 
def getStudent(id):
    for student in Student.objects.all():
        if (student.id == id):
            return student
    return null