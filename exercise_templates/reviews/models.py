from django.db import models
from books.models import Book


class Review(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    rating = models.DecimalField(
        max_digits=4,
        decimal_places=2,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    def __str__(self):
        return f"{self.author} - {self.book.title} - {self.body}"
