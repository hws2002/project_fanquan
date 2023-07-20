from django.shortcuts import render
from rest_framework import generics,status
from django.http import HttpResponse,JsonResponse
from .models import Event,Category
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer

from .serializers import EventSerializer,CreateEventSerializer

# Create your views here.
def index(request):
    return render(request,'event_hall_index.html')

def event_detail(request,event_id):
    return HttpResponse("You are looking at event %s." % event_id)


class EventView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.order_by('id')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class CreateEventView(APIView):
    # override default methods
    serializer_class = CreateEventSerializer
    
    def post(self,request,format=None):
        # use session info
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
            
        # take data and serialize it
        serailizer = self.serializer_class(data=request.data)
        if serailizer.is_valid():
            event_name = serailizer.data.get('event_name')
            
            event_description = serailizer.data.get('event_description')
            category_id = serailizer.data.get('category_id')
            capacity = serailizer.data.get('capacity')
            host = self.request.session.session_key
            
            queryset = Event.objects.filter(event_name=event_name)
            if(queryset.exists()):
                return Response({'Bad Request': 'Event with this name already exists'},status=status.HTTP_400_BAD_REQUEST)
            else :
                event = Event(event_name=event_name,category_id=category_id,event_description=event_description,capacity=capacity,joined = 1)
                event.save()
                return Response(EventSerializer(event).data,status=status.HTTP_201_CREATED)
        else :
            print(serailizer.errors)
        
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

