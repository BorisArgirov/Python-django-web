from django.shortcuts import render, get_object_or_404

from review.models import Review


def recent_reviews(request):
    reviews = Review.objects.filter(is_published=True).order_by('-created_at')[:5]

    context = {
        'reviews': reviews,
        'page_title': 'Recent Reviews',
    }

    return render(request, 'review/list.html', context)

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)

    context = {
        'review': review,
        'page_title': f"{review.author}\'s review on {review.destination.name}",
    }

    return render(request, 'review/detail.html', context)

