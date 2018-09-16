from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='login/')),
    path('login/', auth_views.LoginView.as_view(
        template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='auth/logout.html', next_page='/catalogo/'), name='logout'),
    path('registrar/', views.registrar_form, name='registrar')
]