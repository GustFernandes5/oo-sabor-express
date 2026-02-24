from modelos.avaliacao import Avaliacao

"""
nome = str
categoria = str
ativo = bool
"""


# vars ao usar no print exibe um dicionario com os atributos de uma classe
class Restaurante:
    restaurantes = []

    def __init__(self, nome: str, categoria: str):
        self._nome = nome.title()
        self._categoria = categoria.title()
        self._ativo = False  # ._ torna o atributo privado
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f"nome:  {self._nome} | categoria: {self._categoria}"

    @classmethod
    def listar_restaurantes(cls):
        print(f"{"Nome restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} |{"Status"}")
        for restaurante in cls.restaurantes:
            print(
                f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}"
            )

    @property
    def ativo(self):
        return f"{"☑" if self._ativo else "☐"}"

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_notas, 1)
        return media
