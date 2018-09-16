from django import forms
from django.contrib.auth.models import User

class RegistrarForm(forms.Form):
    nome_de_usuario = forms.CharField(label='Nome de usuário', max_length=254)
    email = forms.EmailField()
    senha = forms.CharField(max_length=16, widget=forms.PasswordInput)
    rep_senha = forms.CharField(label='Repita a senha', max_length=16, widget=forms.PasswordInput)
    nome = forms.CharField(max_length=100, label="Nome")
    sobrenome = forms.CharField(max_length=100)

    def clean_nome_de_usuario(self):
        cleaned_nome_de_usuario = self.cleaned_data['nome_de_usuario']

        for usuario in User.objects.all():
            if cleaned_nome_de_usuario == usuario.username:
                raise forms.ValidationError("Nome de usuário já existe")
        return cleaned_nome_de_usuario
    
    def clean_email(self):
        cleaned_email = self.cleaned_data['email']

        for usuario in User.objects.all():
            if cleaned_email == usuario.username:
                raise forms.ValidationError("Email já existe")
        return cleaned_email

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        rep_senha = cleaned_data.get("rep_senha")

        if senha != rep_senha:
            raise forms.ValidationError("Senhas não se batem.")
