from django.urls import path
from photos import views

app_name = 'photos'

urlpatterns = [
    path('add/', views.photo_add, name='add'),
    path('edit/<int:pk>/', views.photo_edit, name='edit'),
    path('details/<int:pk>/', views.photo_details, name='details'),
]