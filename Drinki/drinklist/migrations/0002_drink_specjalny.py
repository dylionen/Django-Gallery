# Generated by Django 2.0.6 on 2018-06-25 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinklist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='specjalny',
            field=models.BooleanField(default=False),
        ),
    ]
