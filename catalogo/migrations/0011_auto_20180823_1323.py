# Generated by Django 2.0.7 on 2018-08-23 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0010_auto_20180823_1315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imovel',
            old_name='imagens',
            new_name='imagem',
        ),
    ]
