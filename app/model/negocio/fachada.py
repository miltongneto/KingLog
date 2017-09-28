from .controladorCliente import ControladorCliente
class Fachada(object):

	controladorCliente = None

	def __init__(self):
		self.controladorCliente = ControladorCliente()

	def cadastrarCliente(self, cliente):
		print("Fachada " + cliente.nome)
		self.controladorCliente.cadastrarCliente(cliente)
		

