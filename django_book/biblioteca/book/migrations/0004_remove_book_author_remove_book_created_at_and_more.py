# Generated by Django 5.1.1 on 2024-09-17 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_remove_book_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='book',
            name='title',
        ),
        migrations.RemoveField(
            model_name='book',
            name='year',
        ),
    ]
