from django import forms

from reviews.models import Review


class ReviewFormBasic(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewCreateForm(ReviewFormBasic):
    ...


class ReviewEditForm(ReviewFormBasic):
    ...


class ReviewDeleteForm(ReviewFormBasic):
    ...
