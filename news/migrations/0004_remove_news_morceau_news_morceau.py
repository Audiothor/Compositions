# Generated by Django 4.2.11 on 2024-08-07 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('morceaux', '0033_alter_morceau_music_file'),
        ('news', '0003_alter_news_end_publication_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='morceau',
        ),
        migrations.AddField(
            model_name='news',
            name='morceau',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='morceaux.morceau'),
        ),
    ]
