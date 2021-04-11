from django.shortcuts import render
from .forms import CsvModelFrom
from .models import Csv
import csv
from courses.models import Course
# from django.http import HttpResponse
# Create your views here.

def upload_file_view(request):
  form = CsvModelFrom(request.POST or None, request.FILES or None)
  if form.is_valid():
    form.save()
    form = CsvModelFrom()
    obj = Csv.objects.get(activated=False)
    with open(obj.file_name.path, 'r') as f:
      reader = csv.reader(f)

      for i, row in enumerate(reader):
        if i ==0:
          pass
        else:
          row = ''.join(row)
          # row = row.replace(".", ' ')
          row = row.split()
          course = row[0]
          skills = row[1]
          for skill in row[2:]:
            skills += f" {skill}"
          
          Course.objects.create(
            name = course,
            skill = skills
          )
          
      obj.activated = True
      obj.save()
  return render(request, 'csvs/upload.html', {'form': form})