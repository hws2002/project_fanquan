from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return render(request,'event_hall_index.html')

def event_detail(request,event_id):
    return HttpResponse("You are looking at event %s." % event_id)
