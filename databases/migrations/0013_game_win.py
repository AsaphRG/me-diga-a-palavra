# Generated by Django 5.1.1 on 2024-10-08 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0012_remove_move_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='win',
            field=models.BooleanField(default=False, verbose_name='Vitória'),
        ),
    ]