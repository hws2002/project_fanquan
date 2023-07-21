from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('event/<str:event_id>',views.index,name='event_detail'),
    path('events/',views.EventView.as_view(),name='all_events'),
    path('create/',views.index),
    
    
    # API ENDPOINTS
    path('new_event/',views.CreateEventView.as_view(),name='new_event'),
    path('categories',views.CategoryView.as_view(),name='categories'),
    path('get-event/',views.GetEvent.as_view(),name='get-events'),
]