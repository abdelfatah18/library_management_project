# Generated by Django 5.1.3 on 2025-01-19 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='available_copies',
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
    ]
