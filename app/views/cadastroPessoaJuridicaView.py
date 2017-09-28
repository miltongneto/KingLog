from django.shortcuts import render, redirect
from django import forms
from app.model.dados.cliente.pessoaJuridica import PessoaJuridica
from app.model.negocio.fachada import Fachada
from app.forms import PessoaJuridicaForm

# Create your views here.

def cadastrarPessoaJuridica(request):
	if request.method == "POST":
		form = PessoaJuridicaForm(request.POST)
		if form.is_valid():
			cliente = form.save(commit = False)
			fachada = Fachada()
			fachada.cadastrarCliente(cliente)	
			return redirect('index')
	else:
		form = PessoaJuridicaForm()
		return render(request, 'app/cadastroPessoaJuridicaTela.html',{'form': form})