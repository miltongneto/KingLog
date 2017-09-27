from django import forms
from app.util.tipoClienteUtil import TipoCliente
from .model.dados.cliente.cliente import Cliente
from .model.dados.cliente.pessoaJuridica import PessoaJuridica
from .model.dados.cliente.pessoaFisica import PessoaFisica

TIPOS_CLIENTE_CHOICES = (
		(TipoCliente.PESSOA_FISICA.value, 'Pessoa fisica'),
		(TipoCliente.PESSOA_JURIDICA.value, 'Pessoa juridica'),
)

class ClienteForm(forms.Form):
	tipo_cliente = forms.ChoiceField(choices = TIPOS_CLIENTE_CHOICES, widget = forms.RadioSelect)

class PessoaJuridicaForm(forms.ModelForm):

	class Meta:
		model = PessoaJuridica
		fields = ('nome', 'email', 'telefone', 'cnpj', 'razaoSocial', 'razaoSocial')

class PessoaFisicaForm(forms.ModelForm):

	class Meta:
		model = PessoaFisica
		fields = ('nome', 'email', 'telefone', 'cpf', 'rg', 'dataNascimento', 'sexo')