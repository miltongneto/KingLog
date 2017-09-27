from .iRepCliente import IRepCliente
class RepClienteBD(IRepCliente):

	def inserir(self, entidade):
		print("Inserir")
		entidade.save()

	def atualizar(self, entidade):
		pass

	def deletar(self, entidade):
		pass