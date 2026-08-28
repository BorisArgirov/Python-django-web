from django.shortcuts import render, get_object_or_404
from reviews.models import Review


def recent_reviews(request):
    reviews = Review.objects.select_related('book').all().order_by('-created_at')

    context = {
        'reviews': reviews,
        'page_title': 'Recent Reviews',
    }

    return render(request, 'reviews/list.html', context)

def review_details(request, pk):
    review = get_object_or_404(
        Review.objects.select_related('book'),
        pk=pk
    )

    context = {
        'review': review,
        'page_title': f"{review.author}'s review on {review.book.title}"
    }

    return render(request, 'reviews/detail.html', context)


