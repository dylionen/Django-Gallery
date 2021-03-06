# Generated by Django 2.0.6 on 2018-06-27 16:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drinklist', '0003_drinkcomments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='drink',
            options={'verbose_name': 'Drink', 'verbose_name_plural': 'Drinki'},
        ),
        migrations.AlterModelOptions(
            name='drinkcomments',
            options={'verbose_name': 'Lista komentarzy', 'verbose_name_plural': 'Lista komentarzy'},
        ),
        migrations.AddField(
            model_name='drinkcomments',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='drink',
            name='czas',
            field=models.FloatField(verbose_name='Czas wykonania'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data dodania'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='nazwa',
            field=models.CharField(max_length=50, verbose_name='Nazwa'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='opis',
            field=models.TextField(verbose_name='Opis'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='poziom',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Poziom'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='skladnik1',
            field=models.CharField(max_length=50, verbose_name='Składnik 1'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='skladnik2',
            field=models.CharField(blank=True, max_length=50, verbose_name='Składnik 2'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='skladnik3',
            field=models.CharField(blank=True, max_length=50, verbose_name='Składnik 3'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='skladnik4',
            field=models.CharField(blank=True, max_length=50, verbose_name='Składnik 4'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='skladnik5',
            field=models.CharField(blank=True, max_length=50, verbose_name='Składnik 5'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='skladnik6',
            field=models.CharField(blank=True, max_length=50, verbose_name='Składnik 6'),
        ),
        migrations.AlterField(
            model_name='drinkcomments',
            name='news',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='drinklist.Drink'),
        ),
    ]
