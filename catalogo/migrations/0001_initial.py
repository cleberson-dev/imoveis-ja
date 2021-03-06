# Generated by Django 2.0.7 on 2018-08-04 14:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.ImageField(upload_to='src/fotos/')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do imóvel')),
                ('preco', models.FloatField(help_text='Em R$', verbose_name='Preço')),
                ('quartos', models.PositiveIntegerField()),
                ('area', models.PositiveIntegerField(help_text='Em m²', verbose_name='Área')),
                ('localizacao', models.CharField(help_text='Rua/Avenida, Bairro, Cidade - Estado', max_length=100, verbose_name='Localização')),
                ('tipo', models.CharField(choices=[('casa_padrao', 'Casa Padrão'), ('casa_condominio', 'Casa de condomínio'), ('casa_vila', 'Casa de vila'), ('flat', 'Flat'), ('cobertura', 'Cobertura'), ('loft', 'Loft'), ('studio', 'Studio'), ('apartamento', 'Apartamento'), ('terreno', 'Terreno Padrão'), ('lot_condo', 'Loteamento/Condomínio')], max_length=100, verbose_name='Tipo de imóvel')),
                ('data_criacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('anunciante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('imagens', models.ManyToManyField(to='catalogo.Foto')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Adicione palavras-chave para descrever pontos principais do imóvel.', max_length=20, unique=True)),
            ],
        ),
    ]
