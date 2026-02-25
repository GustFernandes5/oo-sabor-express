from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa


restaurante_praca = Restaurante("Praça", "Gourmet")

bebida_suco = Bebida("suco de melancia", 5, "grande")

pudim = Sobremesa("pudim", 10, "Doce bom", "200g", "Melhor pudim da city")

prato_paozinho = Prato("paozinho", 2, "O melhor pão da cidade")
bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()


restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(pudim)


def main():
    restaurante_praca.exibir_cardapio


if __name__ == "__main__":
    main()
