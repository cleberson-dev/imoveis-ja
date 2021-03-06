# Generated by Django 2.0.7 on 2018-08-23 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0008_auto_20180823_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='tipo',
            field=models.CharField(choices=[('casa_padrao', 'Casa Padrão'), ('casa_condominio', 'Casa de condomínio'), ('casa_vila', 'Casa de vila'), ('flat', 'Flat'), ('cobertura', 'Cobertura'), ('loft', 'Loft'), ('studio', 'Studio'), ('apartamento', 'Apartamento'), ('terreno', 'Terreno Padrão'), ('lot_condo', 'Loteamento/Condomínio'), ('exemplo', 'Casa abandonada')], max_length=100, verbose_name='Tipo de imóvel'),
        ),
    ]
