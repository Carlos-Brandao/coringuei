# Generated by Django 5.0.6 on 2024-06-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabalho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diaPostado', models.DateField()),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('nota', models.IntegerField()),
                ('comentario', models.TextField()),
            ],
        ),
    ]