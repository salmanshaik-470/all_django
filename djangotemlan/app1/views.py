from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    return  render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def condition(request):
    x = datetime.datetime.now()

    return render(request,'condition.html',context={'n':'shaik salman','a':26,'date': x})

