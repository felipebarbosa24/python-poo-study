#Exercício 2 - Escreva um programa básico semelhante ao Netflix, que permita:
# - Adicionar filmes ou séries a uma lista de favoritos.
# - Visualizar os itens atualmente presentes na lista de favoritos.
# - Não se esqueça de utilizar classes para modelar a solução.

class Produto:
  def __init__(self, titulo, tipo):
    self.titulo = titulo
    self.tipo = tipo

  def mostrar(self):
    print(f"{self.tipo}: {self.titulo}")

class Favoritos:
  def __init__(self):
    self.lista = []

  def adicionar(self, titulo, tipo):
    produto = Produto(titulo, tipo)
    self.lista.append(produto)

  def mostrar(self):
    if len(self.lista) == 0:
      print("Não possui nenhum filme/série adicionada em favoritos!")
    else:
      print("\n---Lista de Favoritos---")
      for produto in self.lista:
        produto.mostrar()

meus_favoritos = Favoritos()
meus_favoritos.adicionar("Stranger Things", "Série")
meus_favoritos.adicionar("Nanatsu No Taizai", "Série")

meus_favoritos.mostrar()