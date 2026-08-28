from datetime import date
from django import forms
from books.models import Book


# class BookFormBasic(forms.Form):
#     title = forms.CharField(
#         max_length=100,
#         widget=forms.TextInput(attrs={'placeholder': 'e. g. Done'})
#     )
#
#     price = forms.DecimalField(
#         max_digits=6,
#         decimal_places=2,
#         min_value=0,
#         widget=forms.NumberInput(attrs={'step' : '2'}),
#         label = 'Price (USD)'
#     )
#     isbn = forms.CharField(max_length=12, min_length=5)
#     genre = forms.ChoiceField(choices=Book.genre_choices)
#     publishing_date = forms.DateField(initial=date.today)
#     description = forms.CharField(widget=forms.Textarea)
#     image_url = forms.URLField()

class BookFormBasic(forms.ModelForm):
    class Meta:
        exclude = ['slug']
        model = Book

class BookCreateForm(BookFormBasic):
    ...

class BookEditForm(BookFormBasic):
    ...

class BookDeleteForm(BookFormBasic):
    ...
