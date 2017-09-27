from django import forms

from .model.dados.cliente.cliente import Cliente

class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente
		fields = ('nome', 'email', 'telefone')