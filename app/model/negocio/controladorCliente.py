from app.model.dados.cliente.cadastroCliente import CadastroCliente

class ControladorCliente(object):

	cadastroCliente = None

	def __init__(self):
		self.cadastroCliente = CadastroCliente()

	def cadastrarCliente(self, cliente):
		self.cadastroCliente.inserir(cliente)