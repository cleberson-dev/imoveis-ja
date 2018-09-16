from django.contrib import admin
from .models import Imovel, Tag

# Register your models here.

admin.site.register(Imovel)
admin.site.register(Tag)