from django.contrib import admin
from .model.dados.cliente.cliente import Cliente
from .model.dados.cliente.pessoaFisica import PessoaFisica
from .model.dados.cliente.pessoaJuridica import PessoaJuridica

# Register your models here.

admin.site.register(Cliente)
admin.site.register(PessoaFisica)
admin.site.register(PessoaJuridica)
