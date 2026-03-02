from modelos.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):

    def __init__(self, nome, preco, tamanho_bebida):
        super().__init__(nome, preco)
        self.tamanho_bebida = tamanho_bebida

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco*0.08)
