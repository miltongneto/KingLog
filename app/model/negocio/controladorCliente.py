from app.model.dados.cliente.cadastroCliente import CadastroCliente
class ControladorCliente(object):
	def cadastrarCliente(self, cliente):
		print("Controlador, cadastrarCliente " + cliente.nome)
		cadastroCliente = CadastroCliente()
		cadastroCliente.inserir(cliente)