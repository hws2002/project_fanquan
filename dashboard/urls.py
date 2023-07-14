from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('group/',views.GroupView.as_view(),name='group_list'),
]
