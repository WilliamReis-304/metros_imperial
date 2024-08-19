from classes import *

# Criando instâncias de Livro e Revista
livro1 = Livro("harry potter", "J.K. Rowling", "Fantasia e Ficção")
revista1 = Revista("Veja", "Editora Abril", "Edição 2015")

# Exibindo informações dos materiais
print("Informações do Livro:")
livro1.exibir_informacoes()

print("\nInformações da Revista:")
revista1.exibir_informacoes()
