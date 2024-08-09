# Generated by Django 4.2.11 on 2024-08-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('morceaux', '0033_alter_morceau_music_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Name')),
                ('type', models.CharField(blank=True, max_length=50, null=True, verbose_name='Type')),
                ('comment', models.TextField(blank=True)),
                ('date_creation', models.DateField(blank=True, null=True)),
                ('start_publication', models.DateField(blank=True, null=True)),
                ('end_publication', models.DateField(blank=True, null=True)),
                ('activated', models.BooleanField(default=True)),
                ('morceau', models.ManyToManyField(to='morceaux.morceau')),
            ],
            options={
                'ordering': ['date_creation'],
            },
        ),
    ]
