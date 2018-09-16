from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from uuid import uuid4


TIPOS_DE_IMOVEIS = (
        ('casa_padrao', 'Casa Padrão'),
        ('casa_condominio', 'Casa de condomínio'),
        ('casa_vila', 'Casa de vila'),
        ('flat', 'Flat'),
        ('cobertura', 'Cobertura'),
        ('loft', 'Loft'),
        ('studio', 'Studio'),
        ('apartamento', 'Apartamento'),
        ('terreno', 'Terreno Padrão'),
        ('lot_condo', 'Loteamento/Condomínio'),
    )

def renomear_imagem(instancia, nome_do_arquivo):
    extensao = nome_do_arquivo.split('.')[-1]
    nome = f'{uuid4()}.{extensao}'
    return 'media/imoveis/' + nome



class Imovel(models.Model):
    
    nome = models.CharField(
        max_length = 100, 
        verbose_name = "Nome do imóvel"
    )

    preco = models.FloatField(
        help_text = "Em R$",
        verbose_name = "Preço"
    )

    quartos = models.PositiveIntegerField()

    banheiros = models.PositiveIntegerField(default=1)

    vagas_estacionamento = models.PositiveIntegerField(
        default=1,
        verbose_name="Vagas de estacionamento",
    )

    area = models.PositiveIntegerField(
        help_text='Em m²', 
        verbose_name='Área',
    )

    localizacao = models.CharField(
        max_length=100, help_text="Rua/Avenida, Bairro, Cidade - Estado",
        verbose_name="Localização"
    )

    tipo = models.CharField(
        max_length=100, 
        verbose_name="Tipo de imóvel", 
        choices=TIPOS_DE_IMOVEIS
    )

    data_criacao = models.DateTimeField(
        auto_now_add=True, 
        editable=False,
        verbose_name="Data de criação"
    )

    descricao = models.TextField(
        verbose_name="Descrição",
        blank = True
    )


    anunciante = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    tags = models.ManyToManyField('Tag')

    imagem = models.ImageField(null=True, blank=True, upload_to=renomear_imagem)




    class Meta:
        ordering = ['-data_criacao']

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('info-imovel', args=[str(self.id)])
    
class Tag(models.Model):
    nome = models.CharField(
        unique=True,
        max_length=20, 
        help_text="Adicione palavras-chave para descrever pontos principais do imóvel.",
    )

    def __str__(self):
        return self.nome
