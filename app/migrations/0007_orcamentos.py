# Generated by Django 3.2.7 on 2021-10-13 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20211013_1749'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orcamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('descricao', models.CharField(max_length=250)),
                ('precoUnitario', models.IntegerField()),
                ('subTotal', models.IntegerField()),
                ('total', models.IntegerField()),
                ('frete', models.IntegerField()),
                ('taxas', models.IntegerField()),
            ],
        ),
    ]
