from django.db import models
from django.forms.fields import DateTimeField
from django.template.defaultfilters import default
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from _overlapped import NULL
from django.template.defaultfilters import default


class ContactMe(models.Model):
    title = models.CharField(max_length=50,verbose_name="Tytuł")
    mail = models.CharField(max_length=50,verbose_name="E-mail")
    author = models.CharField(max_length=50,verbose_name="Autor")
    text = models.TextField(verbose_name="Treść")
    data_dodania = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False);


    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name="Wiadomość do Admina"
        verbose_name_plural="Wiadomości do Admina"
    
