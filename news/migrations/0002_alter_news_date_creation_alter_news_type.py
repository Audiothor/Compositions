# Generated by Django 4.2.11 on 2024-08-05 15:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date_creation',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='type',
            field=models.CharField(choices=[('1', 'New music'), ('2', 'Information'), ('3', 'Concert')], max_length=50),
        ),
    ]
