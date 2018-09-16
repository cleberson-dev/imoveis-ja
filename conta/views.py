from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import RegistrarForm

def registrar_form(request):
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        if form.is_valid():
            nome_de_usuario = form.cleaned_data.get('nome_de_usuario')
            email = form.cleaned_data.get('email')
            senha = form.cleaned_data.get('senha')
            nome = form.cleaned_data.get('nome')
            sobrenome = form.cleaned_data.get('sobrenome')

            User.objects.create_user(
                nome_de_usuario, 
                email, 
                senha,
                first_name = nome,
                last_name = sobrenome
            )

            usuario = authenticate(username=nome_de_usuario, password=senha)
            if usuario is not None:
                login(request, usuario)
                return HttpResponseRedirect('/catalogo/')
            
    else:
        form = RegistrarForm()
    return render(request, 'register.html', {'form': form })