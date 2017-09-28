from django.shortcuts import render, redirect
from django import forms
from app.model.dados.cliente.pessoaFisica import PessoaFisica
from app.model.negocio.fachada import Fachada
from app.forms import PessoaFisicaForm

# Create your views here.

def cadastrarPessoaFisica(request):
	if request.method == "POST":
		form = PessoaFisicaForm(request.POST)
		if form.is_valid():
			cliente = form.save(commit = False)
			print(cliente.cpf)
			#fachada = Fachada()
			#fachada.cadastrarCliente(cliente)
			return redirect('index')
	else:
		form = PessoaFisicaForm()
		return render(request, 'app/cadastroPessoaFisicaTela.html',{'form': form})