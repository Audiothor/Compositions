# Generated by Django 4.2.11 on 2024-04-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morceaux', '0007_alter_morceau_liste_instruments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='morceau',
            name='commentaire',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='morceau',
            name='date_debut',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='morceau',
            name='date_fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='morceau',
            name='documentation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='morceau',
            name='duree',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Durée du morceau'),
        ),
        migrations.AlterField(
            model_name='morceau',
            name='fichier_documentation',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='morceau',
            name='support',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='morceau',
            name='type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
