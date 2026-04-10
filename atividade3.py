class Livro:
    def __init__(self, isbn, titulo, autor, ano):
        self.isbn = isbn
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    
    def __repr__(self):
        return f"{self.titulo}, ({self.ano}) - {self.autor} [ISBN: {self.isbn}]"
    
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro: Livro):
        self.livros.append(livro)

    def listar_livros(self):
        return self.livros

    def buscar_por_isbn(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro
        return None
    
livro1 = Livro("123-4", "São Paulo e o dominio mundial", "Telê Santana", 2005)
livro2 = Livro("567-8", "Palmeiras não tem mundial kk", "Abel Ferreira", 2021)
livro3 = Livro("425-6", "Luciano é idolo", "Luciano", 2026)

biblioteca = Biblioteca()

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

print("Lista de livros na biblioteca")
for livro in biblioteca.listar_livros():
    print(livro)

isbn_busca = "567-8"
livro_encontrado = biblioteca.buscar_por_isbn(isbn_busca)

print("Resultado da busca:")
if livro_encontrado:
    print("Livro encontrado:", livro_encontrado)
else:
    print("Nenhum livro encontrado com esse ISBN")