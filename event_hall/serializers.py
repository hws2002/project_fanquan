from rest_framework import serializers
from .models import Event,Category
from dashboard.serializers import UserSerializer

#
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class EventSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Event
        fields = (
            'event_name', 
            'host', 
            'category', 
            'event_description', 
            'created_at', 
            'capacity', 
            'joined',
        )

# ----------------------------------------
# Nested serializer
# Assuming 
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username')

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name')

# {
#     "event_name": "My Event",
#     "host": {  # Nested dictionary with User fields
#         "id": 1,
#         "username": "user1"
#     },
#     "category": {  # Nested dictionary with Category fields
#         "id": 1,
#         "name": "category1"
#     },
#     "event_description": "This is my event",
#     "created_at": "2021-09-01T00:00:00Z",  # ISO 8601 formatted string
#     "capacity": 10,
#     "joined": 1,
# }
# ----------------------------------------

# Return
# {
#     "event_name": "My Event",
#     "host": 1,  # The id of the User instance
#     "category": 1,  # The id of the Category instance
#     "event_description": "This is my event",
#     "created_at": "2021-09-01T00:00:00Z",  # ISO 8601 formatted string
#     "capacity": 10,
#     "joined": 1,
# }


class CreateEventSerializer(serializers.ModelSerializer):
    host_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    class Meta:
        model = Event
        fields = (
            'event_name', 
            'host_id', 
            'category_id', 
            'event_description', 
            'capacity', 
        )
        
