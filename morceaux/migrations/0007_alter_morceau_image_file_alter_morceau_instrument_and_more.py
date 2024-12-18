# Generated by Django 4.2.11 on 2024-11-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morceaux', '0006_alter_morceau_image_file_remove_morceau_instrument_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morceau',
            name='image_file',
            field=models.FileField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='morceau',
            name='instrument',
            field=models.ManyToManyField(to='morceaux.instrument'),
        ),
        migrations.AlterField(
            model_name='morceau',
            name='music_file',
            field=models.FileField(blank=True, null=True, upload_to='musics'),
        ),
        migrations.AlterField(
            model_name='morceau',
            name='style',
            field=models.ManyToManyField(to='morceaux.style'),
        ),
    ]
