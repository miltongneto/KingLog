from django.shortcuts import render
from .model.dados.cliente.cliente import Cliente

# Create your views here.

def index(request):
	cliente = Cliente(
		nome = "Milton", email = "mvgn@", telefone = "123456"
		)
	return render(request, 'app/index.html', {'nome' : cliente.nome})