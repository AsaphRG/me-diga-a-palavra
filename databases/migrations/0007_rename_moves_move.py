# Generated by Django 5.1.1 on 2024-09-29 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0006_game_theme'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Moves',
            new_name='Move',
        ),
    ]
