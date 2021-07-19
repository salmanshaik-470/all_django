from django.shortcuts import render

from .models import student


# Create your views here.
def index(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')


def student_details(request):
    data = student.objects.all()
    return  render(request,'student.html',{"data":data})

