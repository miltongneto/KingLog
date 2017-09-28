from django.shortcuts import render, redirect
from django import forms
from app.model.dados.cliente.cliente import Cliente
from app.model.negocio.fachada import Fachada
from app.forms import ClienteForm
from app.util.tipoClienteUtil import TipoCliente

# Create your views here.

def index(request):
	cliente = Cliente(
		nome = "Milton", email = "mvgn@", telefone = "123456"
		)
	return render(request, 'app/index.html', {'nome' : cliente.nome})

def cadastrarCliente(request):
	if request.method == "POST":
		form = ClienteForm(request.POST)
		if form.is_valid():
			tipo = form.cleaned_data['tipo_cliente']
			tipo = TipoCliente.PESSOA_FISICA
			if tipo is TipoCliente.PESSOA_FISICA:
				print("PESSOA_FISICA")
				return redirect('cadastroPessoaFisica')
			elif tipo is TipoCliente.PESSOA_JURIDICA:
				print("PESSOA_JURIDICA")
				return redirect('cadastroPessoaJuridica')

			return redirect('index')
	else:
		form = ClienteForm()
		return render(request, 'app/cadastroClienteTela.html',{'form': form})

def cadastrarEndereco(request,  clienteArg):
	print("chegou")
	return render(request, 'app/index.html')