# Generated by Django 5.0 on 2024-07-14 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='price',
        ),
    ]
