"""
	URLs do app
"""
from django.conf.urls import url
from .views import cadastroClienteView
from .views import cadastroPessoaJuridicaView
from .views import cadastroPessoaFisicaView
 
urlpatterns = [
	url(r'^$', cadastroClienteView.index, name='index'),
	url(r'^CadastrarCliente/$', cadastroClienteView.cadastrarCliente, name='cadastroCliente'),
	url(r'^CadastrarCliente/PessoaJuridica/$', cadastroPessoaJuridicaView.cadastrarPessoaJuridica, name='cadastroPessoaJuridica'),
	url(r'^CadastrarCliente/PessoaFisica/$', cadastroPessoaFisicaView.cadastrarPessoaFisica, name='cadastroPessoaFisica'),
	url(r'^CadastrarCliente/Endereco/$', cadastroClienteView.cadastrarEndereco, name='cadastroEndereco'),
	]