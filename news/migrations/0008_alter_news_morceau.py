# Generated by Django 4.2.11 on 2024-08-08 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('morceaux', '0033_alter_morceau_music_file'),
        ('news', '0007_alter_news_morceau'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='morceau',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='morceau', to='morceaux.morceau'),
        ),
    ]
