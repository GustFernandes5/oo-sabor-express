from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")

restaurante_praca.receber_avaliacao("Gui", 5)
restaurante_praca.receber_avaliacao("Lais", 4.7)



def main():

    print("\t\t\t\tRestaurantes:")
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()






# restaurante_mexicano = Restaurante("Mexican Food", "Mexicana")
# restaurante_japones = Restaurante("Japa", "Japonesa")
# restaurante_mexicano.alternar_estado()