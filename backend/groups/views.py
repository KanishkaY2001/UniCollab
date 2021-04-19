from django.shortcuts import render
from django.http import JsonResponse

from .models import Group
# Create your views here.
def getGroupById(request, id=id):
  group = {}
  for g in Group.objects.all():
    if (g.id == id):
      group = g.name
      break
  return JsonResponse(group, safe=False)

def index(request, id=id):
  groups = []
  for group in Group.objects.all():
      groups.append({
        'name': group.name
      })
  return JsonResponse(groups, safe=False)
    