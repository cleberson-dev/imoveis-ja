# Generated by Django 2.0.7 on 2018-08-05 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_auto_20180804_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imovel',
            name='imagens',
        ),
        migrations.AddField(
            model_name='imovel',
            name='imagens',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='vagas_estacionamento',
            field=models.PositiveIntegerField(default=1, verbose_name='Vagas de estacionamento'),
        ),
        migrations.DeleteModel(
            name='Foto',
        ),
    ]