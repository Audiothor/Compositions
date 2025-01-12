# Generated by Django 4.2.11 on 2024-11-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morceaux', '0003_remove_morceau_instrument_remove_morceau_style_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='morceau',
            name='instrument',
        ),
        migrations.RemoveField(
            model_name='morceau',
            name='style',
        ),
        migrations.AddField(
            model_name='morceau',
            name='instrument',
            field=models.ManyToManyField(blank=True, to='morceaux.instrument'),
        ),
        migrations.AddField(
            model_name='morceau',
            name='style',
            field=models.ManyToManyField(blank=True, to='morceaux.style'),
        ),
    ]
