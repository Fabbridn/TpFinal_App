# Generated by Django 5.2.2 on 2025-06-06 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='emisor_id',
            new_name='emisor',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='receptor_id',
            new_name='receptor',
        ),
    ]
