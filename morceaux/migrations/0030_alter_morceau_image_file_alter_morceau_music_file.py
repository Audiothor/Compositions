# Generated by Django 4.2.11 on 2024-07-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morceaux', '0029_remove_morceau_work_directory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morceau',
            name='image_file',
            field=models.FileField(blank=True, upload_to='static/medias/images/'),
        ),
        migrations.AlterField(
            model_name='morceau',
            name='music_file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
