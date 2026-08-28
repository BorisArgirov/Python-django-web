from django.shortcuts import redirect, render

from reviews.forms import ReviewCreateForm, ReviewDeleteForm, ReviewEditForm
from reviews.models import Review


def review_form(request):
    reviews = Review.objects.select_related('book').order_by('-id')
    context = {'reviews': reviews}
    return render(request, 'reviews/review_form.html', context)


def add_review(request):
    form = ReviewCreateForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('reviews:review_form')

    context = {'form': form}
    return render(request, 'reviews/create.html', context)


def review_edit(request, pk):
    review = Review.objects.get(pk=pk)
    form = ReviewEditForm(request.POST or None, instance=review)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('reviews:review_form')

    context = {'form': form}
    return render(request, 'reviews/edit.html', context)


def review_delete(request, pk):
    review = Review.objects.get(pk=pk)
    form = ReviewDeleteForm(request.POST or None, instance=review)

    if request.method == 'POST' and form.is_valid():
        review.delete()
        return redirect('reviews:review_form')

    context = {'form': form}
    return render(request, 'reviews/delete.html', context)
