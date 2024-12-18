# Generated by Django 4.2.11 on 2024-11-22 15:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('morceaux', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Name')),
                ('type', models.CharField(choices=[('', ''), ('New music', 'New music'), ('Information', 'Information'), ('Concert', 'Concert')], max_length=50)),
                ('comment', models.TextField(blank=True)),
                ('order', models.IntegerField(blank=True, default=1)),
                ('date_creation', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('start_publication', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('end_publication', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('activated', models.BooleanField(default=True)),
                ('morceau', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='morceaux.morceau')),
            ],
            options={
                'ordering': ['date_creation'],
            },
        ),
    ]
