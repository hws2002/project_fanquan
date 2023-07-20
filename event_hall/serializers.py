from rest_framework import serializers
from .models import Event



class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'event_name', 
            # 'host_id', 
            # 'category_id', 
            'event_description', 
            'created_at', 
            'capacity', 
            'joined'
        )
        

class CreateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'event_name', 
            # 'host_id', 
            # 'category_id', 
            'event_description', 
            'capacity', 
        )