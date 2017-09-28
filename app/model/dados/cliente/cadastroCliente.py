from .repClienteBD import RepClienteBD

class CadastroCliente(object):
	
	repClienteBD = None

	def __init__(self):
		self.repClienteBD = RepClienteBD()

	def inserir(self, cliente):		
		self.repClienteBD.inserir(cliente)
