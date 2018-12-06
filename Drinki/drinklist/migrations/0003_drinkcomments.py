# Generated by Django 2.0.6 on 2018-06-25 22:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drinklist', '0002_drink_specjalny'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Treść')),
                ('author', models.CharField(blank=True, max_length=255, verbose_name='Autor')),
                ('news', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drinklist.Drink')),
            ],
        ),
    ]
