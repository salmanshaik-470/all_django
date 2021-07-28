from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def add_event(request):
    if request.method == 'POST':
        fm=emp(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = emp()
        reg = Management_Employee.objects.all()
        return render(request,'base.html',{'form':fm,'data':reg})

def delete_data(request,id):
    if request.method == 'POST':
        pi=Management_Employee.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')

def update(request,id):
    if request.method == 'POST':
        data = Management_Employee.objects.get(pk=id)
        fm = emp(request.POST,instance=data)
        if fm.is_valid():
            fm.save()
            messages.info(request,"You have updated Successfully!!")
            return HttpResponseRedirect("/")

    else:
        data = Management_Employee.objects.get(pk=id)
        fm = emp(instance=data)
        return render(request,'update.html',{'fm':fm})


def signuppage(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'You have Succesfully signed up!')
            return HttpResponseRedirect('/')

    else:
        form = signupform()
        return render(request,'signupform.html',{'form':form})

def loginpage(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                user = fm.cleaned_data['username']
                pwd = fm.cleaned_data['password']
                user = authenticate(username=user,password=pwd)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in Successfully')
                    return HttpResponseRedirect('/profile')
            else:
                messages.warning(request,"Entered username or password is not valid")
                return HttpResponseRedirect('/login/')

        else:
            fm = AuthenticationForm()
        return render(request,'loginpage.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect('/login/')