class Carro:
    def __init__(self, modelo: str, cor: str, ano: int):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f"Modelo: {self.modelo} | Cor: {self.cor} | Ano: {self.ano}"


uno_mille = Carro("Uno", "Azul Escuro", 2001)

# print(uno_mille)


class Pessoa:
    def __init__(self, nome: str, idade: int, profissao: str):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f"Nome: {self.nome}, idade: {self.idade}, profissão: {self.profissao}"

    def aniversario(self):
        self.idade += 1

    def saudacao(self):
        return f" Olá eu me chamo {self.nome}, tenho {self.idade} anos e trabalho como {self.profissao}"


gustavo = Pessoa("Gustavo", 19, "Analista")
print(gustavo)
gustavo.aniversario()
print(gustavo.saudacao())
