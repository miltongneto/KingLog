from .controladorCliente import ControladorCliente
class Fachada(object):

	def cadastrarCliente(self, cliente):
		print("Fachada " + cliente.nome)
		controlador = ControladorCliente()
		controlador.cadastrarCliente(cliente)
		

