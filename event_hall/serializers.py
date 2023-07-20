from rest_framework import serializers
from .models import Event,Category

#
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

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
        
