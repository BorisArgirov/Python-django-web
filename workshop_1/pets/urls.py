from django.urls import path

from pets import views

app_name = 'pets'

urlpatterns = [
    path('add/', views.pet_add, name='add'),
    path('edit/<username>/pet/<slug:pet_slug>/', views.pet_edit, name='edit'),
    path('details/<username>/pet/<slug:pet_slug>/', views.pet_details, name='details'),
    path('delete/<username>/pet/<slug:pet_slug>/', views.pet_delete, name='delete'),
]