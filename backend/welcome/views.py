from django.shortcuts import render
from students.models import Student
from django.http import JsonResponse
from datetime import datetime
import json

# Create your views here.

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
                result = { "id" : student.id }
            break
    return JsonResponse(result, safe=False)
        
