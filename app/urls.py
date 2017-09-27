"""
	URLs do app
"""
from django.conf.urls import url
from .views import cadastroClienteView
 
urlpatterns = [
	url(r'^$', cadastroClienteView.index, name='index'),
	url(r'^CadastrarCliente/$', cadastroClienteView.cadastrarCliente, name='cadastroCliente'),
	]