from django.forms import ModelForm
from .models import Imovel

class ImovelForm(ModelForm):
    class Meta:
        model = Imovel
        fields = [
            'nome',
            'tipo', 
            'quartos', 
            'banheiros', 
            'vagas_estacionamento', 
            'preco',
            'area',
            'localizacao',
            'descricao', 
            'tags',
            'imagem'
        ]