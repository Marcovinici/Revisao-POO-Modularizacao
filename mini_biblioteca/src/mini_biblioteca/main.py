from .livros import Livro
from .usuarios import Usuario
from .emprestimos import Emprestimo

user1 = Usuario("vinicius", "123")
livro1 = Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", "023")
emprestimo = Emprestimo(livro1, user1)

print(emprestimo)