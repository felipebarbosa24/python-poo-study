class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = int(idade)  # garante que será número

    def mostrar_aluno(self):
        print(f"Nome do aluno: {self.nome}\nIdade: {self.idade}")

class Escola:
    def comparar_idade(self, aluno):
        if aluno.idade < 0:
            print("Dados inválidos!")
        elif aluno.idade >= 18:
            print(f"{aluno.nome}, sua idade é {aluno.idade}, então você pode estudar de manhã, tarde e noite.")
        else:
            print(f"{aluno.nome}, como é menor de idade, poderá estudar somente de manhã e tarde.")

# --- Teste ---
aluno1 = Aluno("Pedro", 18)
escola = Escola()

aluno1.mostrar_aluno()
escola.comparar_idade(aluno1)
