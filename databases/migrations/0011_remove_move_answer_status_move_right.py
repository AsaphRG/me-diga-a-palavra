# Generated by Django 5.1.1 on 2024-10-07 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0010_remove_game_status_game_finished'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='move',
            name='answer_status',
        ),
        migrations.AddField(
            model_name='move',
            name='right',
            field=models.BooleanField(default=False, verbose_name='Certo'),
        ),
    ]
