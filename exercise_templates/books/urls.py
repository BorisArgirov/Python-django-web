from django.urls import path, include
from .views import landing_page, books_list, book_detail

app_name = 'books'

books_patterns = [
    path('', books_list, name='list'),
    path('<slug:slug>', book_detail, name='detail'),
]
urlpatterns = [
    path('', landing_page, name='Home'),
    path('books/', include(books_patterns))
]