from django.shortcuts import render, redirect
from books.forms import BookFormBasic, BookDeleteForm, BookEditForm
from books.models import Book


def book_form(request):
    books = Book.objects.order_by('-id')
    context = {'books': books}
    return render(request, 'books/book_form.html', context)
def add_book(request):
    form = BookFormBasic(request.POST or None)
    if request.method == 'POST' and form.is_valid():

        form.save()
        return redirect('books:book_form')

    context = {'form': form}
    return render(request, 'books/create.html', context)

def book_edit(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookEditForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():

        form.save()
        return redirect('books:book_form')

    context = {'form': form}
    return render(request, 'books/edit.html', context)

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookDeleteForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():

        book.delete()
        return redirect('books:book_form')

    context = {'form': form}
    return render(request, 'books/delete.html', context)

