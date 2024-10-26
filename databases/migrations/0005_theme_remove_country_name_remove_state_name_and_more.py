# Generated by Django 5.1.1 on 2024-09-29 11:15

import django.db.models.deletion
import django.utils.timezone
import encrypted_model_fields.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('databases', '0004_customuser_sex'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_name', models.CharField(max_length=255, verbose_name='Tema')),
            ],
        ),
        migrations.RemoveField(
            model_name='country',
            name='name',
        ),
        migrations.RemoveField(
            model_name='state',
            name='name',
        ),
        migrations.AddField(
            model_name='country',
            name='country_name',
            field=models.CharField(default='', max_length=255, verbose_name='Nome do País'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='state',
            name='state_name',
            field=models.CharField(default='', max_length=255, verbose_name='Nome do estado'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='country',
            name='ddi',
            field=models.CharField(max_length=255, verbose_name='DDI'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='birth_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='databases.country', verbose_name='País'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='sex',
            field=models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, null=True, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='databases.state', verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='state',
            name='ddd',
            field=models.CharField(max_length=255, verbose_name='DDD'),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_word', encrypted_model_fields.fields.EncryptedCharField(verbose_name='Palavra secreta')),
                ('discovered_word', models.CharField(max_length=255, verbose_name='Palavra descoberta')),
                ('status', models.BooleanField(default=False, verbose_name='Status')),
                ('started_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Início')),
                ('finished_at', models.DateTimeField(blank=True, null=True, verbose_name='Fim')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Jogador')),
            ],
        ),
        migrations.CreateModel(
            name='Moves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=1, verbose_name='Letra')),
                ('time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Hora da jogada')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Jogador')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=255, verbose_name='Palavra')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='databases.theme', verbose_name='Tema')),
            ],
        ),
    ]