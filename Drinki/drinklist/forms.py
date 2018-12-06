from django import forms
from .models import DrinkComments

class CommentForm(forms.ModelForm):
    class Meta:
        model=DrinkComments
        fields = ('news','text','author',)