from .repClienteBD import RepClienteBD
class CadastroCliente(object):
	def inserir(self, cliente):
		print("Cadastrar cliente " + cliente.nome)
		repClienteBD = RepClienteBD()
		repClienteBD.inserir(cliente)
