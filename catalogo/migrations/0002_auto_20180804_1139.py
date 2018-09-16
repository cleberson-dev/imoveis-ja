# Generated by Django 2.0.7 on 2018-08-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='tags',
            field=models.ManyToManyField(to='catalogo.Tag'),
        ),
        migrations.AlterField(
            model_name='foto',
            name='arquivo',
            field=models.ImageField(upload_to='catalogo/static/img'),
        ),
    ]
