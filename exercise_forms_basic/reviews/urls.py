from django.urls import path
from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('delete/<int:pk>/', views.review_delete, name='delete'),
    path('edit/<int:pk>/', views.review_edit, name='edit'),
    path('create/', views.add_review, name='create_review'),
    path('', views.review_form, name='review_form'),
]
