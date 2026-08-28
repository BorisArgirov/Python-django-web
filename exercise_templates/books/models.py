from random import choices

from django.core.validators import MinLengthValidator
from django.db import models
from django.template.defaultfilters import slugify


class Book(models.Model):
    genre_choices = (
        ("Fiction", "Fiction"),
        ("Non-Fiction", "Non-Fiction"),
        ("Fantasy", "Fantasy"),
        ("Science", "Science"),
        ("Mystery", "Mystery"),
        ("Romance", "Romance"),
    )
    title = models.CharField(max_length = 50, unique = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    isbn = models.CharField(
        max_length = 12,
        unique = True,
        validators = [
            MinLengthValidator(12),
        ]
    )
    genre = models.CharField(
        choices = genre_choices,
    )
    publish_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField()
    updated_at = models.DateTimeField(auto_now = True)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
    )
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.genre}"
