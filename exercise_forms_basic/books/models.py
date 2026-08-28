from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


class Book(models.Model):
    genre_choices = (
        ("Fiction", "Fiction"),
        ("Non-Fiction", "Non-Fiction"),
        ("Fantasy", "Fantasy"),
        ("Science", "Science"),
        ("Mystery", "Mystery"),
        ("Romance", "Romance"),
        ("Other", "Other"),
    )

    language_choices = (
        ("Bulgarian", "Bulgarian"),
        ("English", "English"),
        ("French", "French"),
        ("German", "German"),
        ("Other", "Other"),
    )

    title = models.CharField(
        max_length=200,
        unique=True,
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
    )

    isbn = models.CharField(
        max_length=12,
        unique=True,
        validators=[MinLengthValidator(5)],
    )

    genre = models.CharField(
        max_length=20,
        choices=genre_choices,
    )

    language = models.CharField(
        max_length=20,
        choices=language_choices,
    )

    pages = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    is_available = models.BooleanField(
        default=True,
    )

    publishing_date = models.DateField()

    description = models.TextField()

    image_url = models.URLField()

    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):

    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)
