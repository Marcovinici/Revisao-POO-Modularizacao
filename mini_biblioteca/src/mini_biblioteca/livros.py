class Livro:
    def __init__(self, titulo: str, autor: str, codigo: str, disponivel: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = disponivel

    @classmethod
    def novo_livro(cls, titulo: str, autor: str, codigo: str, livros: AllLivros):
        if codigo in livros.codigos:
            raise ValueError
        livros.codigos.append(codigo)
        return Livro(titulo, autor, codigo)

class AllLivros:
    def __init__(self):
        self.codigos = []

    def existe_livro(self, codigo: str) -> bool:
        if codigo in self.codigos:
            return True
        return False

    def adiciona_livro(self, codigo: str) -> None:
        self.codigos.append(codigo)