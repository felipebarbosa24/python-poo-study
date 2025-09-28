# Crie duas classes em Python:

# - Componente: Representa um componente de hardware de um computador (por exemplo: CPU, RAM, HD).
# - Computador: Representa um computador que possui vários componentes.
# - Requisitos: Utilize composição: a classe Computador deve conter objetos da classe Componente.

class Componente:
  def __init__(self, tipo, marca, modelo):
    self.tipo = tipo
    self.marca = marca
    self.modelo = modelo

  def mostrar(self):
    print(f"Tipo: {self.tipo}, marca: {self.marca} e modelo: {self.modelo}")

class Computador:
  def __init__(self):
    self.componentes = []

  def adicionar_componente(self, tipo, marca, modelo): #adicionar validação (bônus)
    componente = Componente(tipo, marca, modelo)
    self.componentes.append(componente)

  def remover_componente(self, tipo):
    for item in self.componentes:
      if item.tipo == tipo:
        self.componentes.remove(item)
        break

  def exibir_componentes(self):
    if len(self.componentes) == 0:
      print("Não há nenhum componente cadastrado")
    else:
      for componente in self.componentes:
        componente.mostrar()

pc = Computador()
pc.adicionar_componente("cpu", "AMD", "R7-5800x")

pc.exibir_componentes()
pc.remover_componente("cpu")

pc.exibir_componentes()