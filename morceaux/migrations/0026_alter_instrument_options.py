# Generated by Django 4.2.11 on 2024-07-24 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('morceaux', '0025_alter_morceau_instrument'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instrument',
            options={'ordering': ['nom']},
        ),
    ]
