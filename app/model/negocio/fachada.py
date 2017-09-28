from .controladorCliente import ControladorCliente
class Fachada(object):

	instance = None
	controladorCliente = None

	def __new__(cls):
		if cls.instance is None:
			cls.instance = super(Fachada,cls).__new__(cls)
		return cls.instance

	def __init__(self):
		self.controladorCliente = ControladorCliente()

	def cadastrarCliente(self, cliente):
		self.controladorCliente.cadastrarCliente(cliente)
		

