from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    # User authentication
    path('',include('django.contrib.auth.urls')),
    path('login_user',views.login_user,name='login'),
    # path('group/',views.GroupView.as_view(),name='group_list'),
]