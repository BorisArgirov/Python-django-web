from django.urls import path
from destination.views import index, destinations_list, destination_detail, redirect_home

urlpatterns = [
    path('', index, name='index'),
    path('redirect-home/', redirect_home, name='redirect_home'),
    path('destinations/', destinations_list, name='destinations_list'),
    path('destinations/', destinations_list, name='list'),
    path('destinations/detail/<slug:slug>/',destination_detail, name = 'destination_detail')
]