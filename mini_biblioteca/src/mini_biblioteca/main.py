from .livros import Livro, AllLivros
from .usuarios import Usuario, AllUsuarios
from .emprestimos import Emprestimo

estantes = AllLivros()
leitores = AllUsuarios()
user1 = Usuario.novo_usuario("vinicius", "123", leitores)
livro1 = Livro.novo_livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", "023", estantes)
emprestimo1 = Emprestimo(livro1, user1)

print(emprestimo1)

user2 = Usuario.novo_usuario("joão", "1234", leitores)

print(leitores)