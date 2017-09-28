from .controladorCliente import ControladorCliente
class Fachada(object):

	controladorCliente = None

	def __init__(self):
		self.controladorCliente = ControladorCliente()

	def cadastrarCliente(self, cliente):
		self.controladorCliente.cadastrarCliente(cliente)
		

