class Livro:
    livros = []

    def __init__(self, titulo: str, autor: str, ano_publicaco: int):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicaco
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f"Título : {self._titulo.ljust(25)} | Autor: {self._autor.ljust(25)} | Ano publicação: {str(self._ano_publicacao).ljust(25)} | Status: {self.disponivel}"

    def emprestar(self):
        if self._disponivel:
            self._disponivel = False

    @property
    def disponivel(self):
        return f"Disponível" if self._disponivel else "Indisponível"

    @staticmethod
    def verificar_disponibilidade(ano_publicacao: int):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano_publicacao and livro.disponivel]

        return livros_disponiveis        

        # for livro in cls.livros:
        #     if livro._ano_publicacao == ano_publicacao:
        #         cls.livros.append(livro)


