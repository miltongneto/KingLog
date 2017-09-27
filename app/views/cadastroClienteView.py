from django.shortcuts import render, redirect
from app.model.dados.cliente.cliente import Cliente
from app.model.negocio.fachada import Fachada
from app.forms import ClienteForm

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
			cliente = form.save(commit = False)
			fachada = Fachada()
			fachada.cadastrarCliente(cliente)	
			return redirect('index')
	else:
		form = ClienteForm()
		return render(request, 'app/cadastroClienteTela.html',{'form': form})