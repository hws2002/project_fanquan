from django.shortcuts import render
from django.http import HttpResponse
# from rest_framework import generics
from .serializers import GroupSerializer
from .models import Group
# Create your views here.

# if has app-level static file sand templates, render templates like so 
# def my_view(request):
#     return render(request, 'dashboard/index.html')

# if has project-level static file sand templates, render templates like so
# def index(request):
#      return render(request, 'dashboard_index.html')

def index(request, *args, **kwargs):
    return render(request,'dashboard_index.html')

# class GroupView(generics.ListCreateAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer