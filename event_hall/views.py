from django.shortcuts import render
from rest_framework import generics,status
from django.http import HttpResponse,JsonResponse
from .models import Event,Category
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer
from .serializers import EventSerializer,CreateEventSerializer,CategorySerializer
# load user model
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def index(request,*args,**kwargs):
    return render(request,'event_hall_index.html')

def event_detail(request,event_id):
    return HttpResponse("You are looking at event %s." % event_id)


class EventView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# Get Event details
class GetEvent(APIView):
    serializer_class = EventSerializer
    lookup_url_kwarg = 'event_id'
    
    def get(self, request, fromat = None):
        event_id = request.GET.get(self.lookup_url_kwarg)
        print(event_id)
        if event_id != None:
            event = Event.objects.filter(id=event_id)
            if len(event) > 0:
                data = EventSerializer(event[0]).data
                data['event_name'] = event[0].event_name
                data['host'] = event[0].host.username
                data['is_host'] = event[0].host.id == 2  # have to change later
                # data['is_host'] = host_id == self.requeest.session.session_key? or host id
                data['category'] = event[0].category.name
                data['event_description'] = event[0].event_description
                data['created_at'] = event[0].created_at
                data['capacity'] = event[0].capacity
                data['joined'] = event[0].joined
                # if self.request.session.exists(self.request.session.session_key):
                #     host = self.request.session.session_key
                #     if event[0].host_id == host:
                #         data['is_host'] = True
                #     if event[0].joined >= event[0].capacity:
                #         data['is_full'] = True
                #     if event[0].joined < event[0].capacity:
                #         data['is_joined'] = True
                return Response(data,status=status.HTTP_200_OK)
            return Response({'Event Not Found':'Invalid event id'},status=status.HTTP_404_NOT_FOUND)
        return Response({'Bad Request':'Event id not found in request'},status=status.HTTP_400_BAD_REQUEST)

#Get all categories
# for Create Event
class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.order_by('id')
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    
# Create Event
class CreateEventView(APIView):
    # override default methods
    serializer_class = CreateEventSerializer
    
    def post(self,request,format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        # take data and serialize it
        serailizer = self.serializer_class(data=request.data)
        if serailizer.is_valid():
            # print("serializer is valid")
            # print(serailizer.data)
            event_name = serailizer.data.get('event_name')
            host_id = 2 # have to change later
            # fetch host info from session
            event_description = serailizer.data.get('event_description')
            category_id = serailizer.data.get('category_id')
            # print(category_id)
            capacity = serailizer.data.get('capacity')
            host = self.request.session.session_key # will get host info from session later
            # print("host : " + host)
            queryset = Event.objects.filter(event_name=event_name)
            if(queryset.exists()):
                return Response({'Bad Request': 'Event with this name already exists'},status=status.HTTP_400_BAD_REQUEST)
            else :
                event = Event(event_name=event_name,host_id = host_id,category_id=category_id,event_description=event_description,capacity=capacity,joined = 1)
                event.save()
                return Response(EventSerializer(event).data,status=status.HTTP_201_CREATED)
        else :
            print(serailizer.errors)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

