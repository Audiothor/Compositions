# Generated by Django 4.2.11 on 2024-04-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morceaux', '0008_alter_morceau_commentaire_alter_morceau_date_debut_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, verbose_name='Nom du style')),
            ],
        ),
    ]
