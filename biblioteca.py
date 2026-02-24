from livro import Livro

eragon = Livro("Dragao", "Alguem", 1988)

eragon.emprestar()

sr_aneis = Livro("Senhor dos anéis", "J.R.R. Tolkien", 1954)
sr_aneis.emprestar()
hobbit = Livro("O Hobbit", "J.R.R. Tolkien", 1988)

# Livro.verificar_disponibilidade(1988)
Livro.livros = [sr_aneis,hobbit,eragon]

ano_especifico = 1988
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(
    f"Livros disponíveis em {ano_especifico}: {', '.join([livro._titulo for livro in livros_disponiveis_ano])}"
)


def main():
    # print(eragon)
    pass


if __name__ == "__main__":
    main()
