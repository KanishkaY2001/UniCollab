from django.shortcuts import render
from django.http import JsonResponse

from .models import Student
# Create your views here.

def index(request):
    students = []

    for student in Student.objects.all():
        students.append({
            'name': student.name,
            'course': student.course,
            'rating': student.rating
        })
    return JsonResponse(students, safe=False)