from .livros import Livro
from .usuarios import Usuario

class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario, ativo: bool = True):
        self.livro = livro
        self.usuario = usuario
        self.ativo = ativo
        # Regras de negócio
        if self.livro.disponivel:
            self.livro.disponivel = False
        else:
            raise ValueError

    def devolver(self):
        self.ativo = False
        self.livro.disponivel = True

    def __str__(self):
        return f"Usuário: {self.usuario.nome}, id: {self.usuario.id_usuario}; \nLivro: {self.livro.titulo}, autor: {self.livro.autor}, código: {self.livro.codigo}; \nEstado do Empréstimo: {self.ativo}"
