from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('complete/',complete,name='complete'),
    path('trash/',trash,name='trash'),
    path('about/',about,name='about'),
    path('update/<int:pk>/',update,name='update'),
    path('completed/<int:pk>/',completed,name='completed'),
    path('hdelete/<int:pk>/',hdelete,name='hdelete')
     
]