# Generated by Django 5.0.2 on 2024-02-19 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Becenev',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nev', models.CharField(max_length=50)),
                ('urhajos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.urhajos')),
            ],
            options={
                'verbose_name': 'Becenev',
                'verbose_name_plural': 'Becenevek',
            },
        ),
    ]
