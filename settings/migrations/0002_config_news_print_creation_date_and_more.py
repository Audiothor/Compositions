# Generated by Django 4.2.11 on 2024-08-07 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='config',
            name='news_print_creation_date',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='config',
            name='news_print_last_five_music',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='config',
            name='news_print_news_type',
            field=models.BooleanField(default=True),
        ),
    ]
