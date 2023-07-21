from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework import generics
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from .serializers import GroupSerializer
# from .models import Group
# Create your views here.

# if has app-level static file sand templates, render templates like so 
# def my_view(request):
#     return render(request, 'dashboard/index.html')

# if has project-level static files and templates, render templates like so
# def index(request):
#      return render(request, 'dashboard_index.html')

def login_user(request):
    if request.method == "POST":
        # username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            #redirect to a success page. (dashboard)
            login(request,user)
            return redirect('')
        else :
            #redirect to a 'invalid login' error message.
            messages.success(request, ("There was an Error Logging In. Please Try Again..."))
            return redirect('login_user')
    return render(request, 'authenticate/login.html',{})    

def index(request, *args, **kwargs):
    return render(request,'dashboard_index.html')

# class GroupView(generics.ListCreateAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer