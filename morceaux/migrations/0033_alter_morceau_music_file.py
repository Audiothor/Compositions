# Generated by Django 4.2.11 on 2024-08-01 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morceaux', '0032_alter_morceau_image_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morceau',
            name='music_file',
            field=models.FileField(blank=True, null=True, upload_to='musics'),
        ),
    ]
