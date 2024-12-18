# Generated by Django 4.2.11 on 2024-11-22 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morceaux', '0005_remove_morceau_instrument_remove_morceau_style_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morceau',
            name='image_file',
            field=models.FileField(blank=True, upload_to='images'),
        ),
        migrations.RemoveField(
            model_name='morceau',
            name='instrument',
        ),
        migrations.AlterField(
            model_name='morceau',
            name='music_file',
            field=models.FileField(blank=True, upload_to='musics'),
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
