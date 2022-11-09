from django.shortcuts import render

from student.models import Student

# Create your views here.

def index(request):
    students = Student.objects.all()
    return render(request, 'index.html', context={'students': students})