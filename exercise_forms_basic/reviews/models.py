from django.db import models
from books.models import Book


class Review(models.Model):
    review_type_choices = (
        ("Text", "Text"),
        ("Video", "Video"),
        ("Audio", "Audio"),
    )

    author = models.CharField(
        max_length=100,
    )

    body = models.TextField()

    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )

    is_verified = models.BooleanField(
        default=False,
    )

    review_type = models.CharField(
        max_length=10,
        choices=review_type_choices,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    def __str__(self):
        return f"{self.author} - {self.book.title}"