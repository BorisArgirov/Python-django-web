from django.urls import path
from books import views
app_name = 'books'
urlpatterns = [
    path('delete/<int:pk>/', views.book_delete, name='delete'),
    path('edit/<int:pk>/', views.book_edit, name='edit'),
    path('create/', views.add_book, name='create_book'),
    path('', views.book_form, name='book_form'),
]
