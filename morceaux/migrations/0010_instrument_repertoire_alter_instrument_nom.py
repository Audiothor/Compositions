# Generated by Django 4.2.11 on 2024-04-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morceaux', '0009_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='repertoire',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Directory'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='nom',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
    ]
