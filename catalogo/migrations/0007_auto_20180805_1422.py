# Generated by Django 2.0.7 on 2018-08-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_auto_20180805_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='imagens',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
