from django.conf import settings
from django.http import HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Imovel
from .forms import ImovelForm


tipos_de_imoveis = Imovel._meta.get_field('tipo').choices

def index(request):
    imoveis = Imovel.objects.all()

    query = request.GET.get('q')
    if query is not None:
        imoveis = imoveis.filter(nome__icontains=query)

    paginador = Paginator(imoveis, 10)
    page_atual_num = request.GET.get('p', 1)
    page_atual_obj = paginador.page(page_atual_num)

    return render(
        request, 
        'generico_lista-imoveis.html', 
        context = {
            'imoveis': page_atual_obj,
            'paginador': paginador,
            'page_atual': int(page_atual_num),
            'tipos_de_imoveis': tipos_de_imoveis,
        }
    )

def lista_tipodeimovel_view(request, tipo):
    imoveis = get_list_or_404(Imovel, tipo=tipo)

    paginador = Paginator(imoveis, 10)
    page_atual_num = request.GET.get('p', 1)
    page_atual_obj = paginador.page(page_atual_num)

    tipo_atual = imoveis[0].get_tipo_display

    return render(
        request, 
        'lista_tipo_imovel.html', 
        context = {
            'imoveis': page_atual_obj,
            'tipo_atual': tipo_atual,
            'paginador': paginador,
            'page_atual': int(page_atual_num),
            'tipos_de_imoveis': tipos_de_imoveis
        }
    )

def info_imovel_view(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk)

    return render(
        request,
        'info-imovel.html',
        context = {
            'imovel': imovel,
        }
    )

@login_required
def imoveis_usuario_view(request):
    usuario = request.user
    imoveis = Imovel.objects.filter(anunciante=usuario)

    paginador = Paginator(imoveis, 10)
    page_atual_num = request.GET.get('p', 1)
    page_atual_obj = paginador.page(page_atual_num)

    return render(
        request, 
        'lista_meus_anuncios.html', 
        context = {
            'imoveis': page_atual_obj, 
            'paginador': paginador, 
            'page_atual': int(page_atual_num)
        }
    )

@login_required
def anunciar_imovel_view(request):
    usuario = request.user

    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES)

        if form.is_valid():
            nome = form.cleaned_data.get('nome')
            preco = form.cleaned_data.get('preco')
            quartos = form.cleaned_data.get('quartos')
            banheiros = form.cleaned_data.get('banheiros')
            vagas = form.cleaned_data.get('vagas_estacionamento')
            area = form.cleaned_data.get('area')
            localizacao = form.cleaned_data.get('localizacao')
            tipo = form.cleaned_data.get('tipo')
            descricao = form.cleaned_data.get('descricao')
            tags = form.cleaned_data.get('tags')
            imagem = form.cleaned_data.get('imagem')


            instancia = Imovel(
                nome=nome,
                preco=preco,
                quartos=quartos,
                banheiros=banheiros,
                vagas_estacionamento=vagas,
                area=area,
                localizacao=localizacao,
                tipo=tipo,
                descricao=descricao,
                anunciante=usuario,
                imagem=imagem
            )
            instancia.save()

            for tag in tags:
                instancia.tags.add(tag)

            return  HttpResponseRedirect(
                reverse('info-imovel', args=[instancia.pk])
            )
    else:
        form = ImovelForm()
    
    return render(request, 'anunciar-imovel.html', { 'form': form })