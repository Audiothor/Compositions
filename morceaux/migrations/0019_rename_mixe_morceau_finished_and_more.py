# Generated by Django 4.2.11 on 2024-07-11 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('morceaux', '0018_rename_music_morceau_music_file_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='morceau',
            old_name='mixe',
            new_name='finished',
        ),
        migrations.RenameField(
            model_name='morceau',
            old_name='termine',
            new_name='mixed',
        ),
    ]
