from django.shortcuts import render
from .models import Users

# Create your views here.


def login(request):
    """if request.method=='POST':
        fullname=request.POST['fname']
        password=request.POST['password']"""
    return render(request, 'login.html')

def registration(request):
    if request.method=='POST':
        fullname=request.POST['fname']
        username=request.POST['username']
        password=request.POST['password']
        user=Users(fullname=fullname, username=username, password=password)
        user.save()
        return render(request, 'test.html')
    else:
        return render(request, 'registration.html')
