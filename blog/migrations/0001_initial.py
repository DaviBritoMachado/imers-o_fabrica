# Generated by Django 4.1.1 on 2022-09-16 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80)),
                ('conteudo', models.TextField()),
                ('date_publicacao', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
