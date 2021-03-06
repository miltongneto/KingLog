# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-09-28 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_pessoafisica_pessoajuridica'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CEP', models.CharField(max_length=8)),
                ('rua', models.CharField(max_length=20)),
                ('numero', models.CharField(max_length=5)),
                ('complemento', models.CharField(max_length=10)),
                ('bairro', models.CharField(max_length=15)),
                ('estado', models.CharField(max_length=15)),
                ('pais', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'endereco',
            },
        ),
    ]
