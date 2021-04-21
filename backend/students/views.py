from django.shortcuts import render
from django.http import JsonResponse

from .serializers import StudentSerializer, EventSerializer
from .models import Student
from rooms.models import Room, Member
from groups.models.groups import Group
from groups.models.groupMembers import GroupMember
from courses.models import Course
from courses.serializers import CourseSerializer

import json
# Create your views here.

def index(request):
    students = []
    for student in Student.objects.all():
        students.append(StudentSerializer(student).data)
    return JsonResponse(students, safe=False)

def user(request, id=id):
    user = {}
    for student in Student.objects.all():
        if (student.id == id):
            user = getUserJson(student)
            break
    return JsonResponse(user, safe=False)

def getUserJson(student):
    photo = json.dumps(str(student.photo))
    events = getCalendar(student)
    courses = getCourses(student)
    result = {
        "name": student.name,
        "bio": student.bio,
        "location": student.location,
        "calendar": events,
        "photo": photo,
        "courses": courses
    }
    return result

def getCalendar(student):
    events = []
    for event in student.calendar.all():
        events.append(EventSerializer(event).data)
    return events

def getCourses(student):
    courses = []
    for course in student.courses.all():
        courses.append(CourseSerializer(course).data)
    return courses

def addCourse(request, id, cname):
    student = getStudent(id)
    coursedata = {}
    for course in Course.objects.all():
        if (course.name == cname):
            student.courses.add(course)
            coursedata = CourseSerializer(course).data
            student.save()
            return JsonResponse(coursedata, safe=False)
    ## ADD IN HERE FOR NEW COURSE CREATION ##
    print(cname)
    return JsonResponse(coursedata, safe=False)

def studentRooms(request, id):
    rooms = []
    for memb in Member.objects.all():
        if (memb.student.id == id): 
            rooms.append({
                "name": memb.room.name,
                "id": memb.room.id
            })
    return JsonResponse(rooms, safe=False)

def studentGroups(request, id):
    groups = []
    for grMemb in GroupMember.objects.all():
        photo = json.dumps(str(grMemb.group.photo))
        if (grMemb.member.id == id or grMemb.group.owner.id == id):
            groups.append({
                "name": grMemb.group.name,
                "id": grMemb.group.id,
                "photo": photo
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
    return None

def register(request, name, email, password):
    student = Student.objects.create(
        name = name,
        email = email, 
        password = password
    )
    student.save()
    result = { student.id }
    return JsonResponse(result, safe=False)

def login(request, email, password):
    result = {}
    for student in Student.objects.all():
        if (student.email == email):
            if (student.password == password):
                info = StudentSerializer(student).data
                result = {
                    "id" : info['id'],
                    "name": info['name'],
                    "photo": info['photo']
                }
            break
    return JsonResponse(result, safe=False)
