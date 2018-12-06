from django.db import models
from django.forms.fields import DateTimeField
from django.template.defaultfilters import default
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from _overlapped import NULL
from django.template.defaultfilters import default

class Drink(models.Model):
    nazwa = models.CharField(max_length=50,verbose_name="Nazwa")
    skladnik1 = models.CharField(max_length=50,verbose_name="Składnik 1")
    skladnik2 = models.CharField(max_length=50,verbose_name="Składnik 2",blank=True)
    skladnik3 = models.CharField(max_length=50,verbose_name="Składnik 3",blank=True)
    skladnik4 = models.CharField(max_length=50,verbose_name="Składnik 4",blank=True)
    skladnik5 = models.CharField(max_length=50,verbose_name="Składnik 5",blank=True)
    skladnik6 = models.CharField(max_length=50,verbose_name="Składnik 6",blank=True)
    specjalny=models.BooleanField(default=False)
    czas = models.FloatField(verbose_name="Czas wykonania")
    poziom = models.FloatField(verbose_name="Poziom",validators=[MinValueValidator(0),
                                       MaxValueValidator(5)])
    opis = models.TextField(verbose_name="Opis")
    data = models.DateTimeField(auto_now_add=True,verbose_name="Data dodania")
    zdjecie = models.ImageField()

    def __str__(self):
        return self.nazwa
    
    class Meta:
        verbose_name="Drink"
        verbose_name_plural="Drinki"
    




class DrinkComments(models.Model):
    news = models.ForeignKey(
    Drink,
    models.SET_NULL,
    blank=True,
    null=True,
    related_name='comments',
)
    text = models.TextField(verbose_name='Treść')
    author = models.CharField(max_length=255,verbose_name='Autor', blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True);
    
    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name="Lista komentarzy"
        verbose_name_plural="Lista komentarzy"
    
    