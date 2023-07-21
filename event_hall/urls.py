from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    
    path('events/<str:event_id>',views.index,name='event_detail'),   
    path('create/',views.index),
    
    # API ENDPOINTS
    path('new_event/',views.CreateEventView.as_view(),name='new_event'),
    path('categories',views.CategoryView.as_view(),name='categories'),
]