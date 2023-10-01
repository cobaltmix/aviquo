from django import forms

from .models import Tag


class TagFilterForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
