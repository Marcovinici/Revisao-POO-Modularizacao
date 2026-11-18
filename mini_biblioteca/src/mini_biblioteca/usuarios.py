class Usuario:
    def __init__(self, nome: str, id_usuario: str):
        self.nome = nome
        self.id_usuario = id_usuario

    @classmethod
    def novo_usuario(cls, nome: str, id_usuario: str, usuarios: AllUsuarios):
        if usuarios.existe_usuario(id_usuario):
            raise ValueError
        usuarios.codigos.append(id_usuario)
        return Usuario(nome, id_usuario)

class AllUsuarios:
    def __init__(self):
        self.codigos = []

    def existe_usuario(self, codigo: str) -> bool:
        if codigo in self.codigos:
            return True
        return False

    def adiciona_livro(self, codigo: str) -> None:
        self.codigos.append(codigo)

    def __str__(self):
        return f"{self.codigos}"