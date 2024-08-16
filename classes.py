# Criando as classes para gerenciamento da biblioteca ---------------------------------------

class Livro:
    _id_counter = 1

    def __init__(self, titulo:str, autor:str):
        self.id = Livro._id_counter
        Livro._id_counter += 1
        self.titulo = titulo
        self.autor = autor
        self.status = 'Disponível'

class Membro:
    def __init__(self, nome:str, numero_membro:str):
        self.nome = nome
        self.numero_membro = numero_membro
        self.historico_emprestimos = []

class Biblioteca:
    def __init__(self):
        self.catalogo = [Livro("O livro do Bill", "Alex Hirsch"), Livro("Harry Potter", "J.K. Rowling")]
        self.membros = [Membro("William","1"), Membro("Avaliador", "10")]

    def adicionar_livro(self, titulo, autor):
        livro = Livro(titulo, autor)
        self.catalogo.append(livro)

    def adicionar_membro(self, nome, numero_membro):
        membro = Membro(nome, numero_membro)
        self.membros.append(membro)

    def emprestar_livro(self, livro_id, numero_membro):
        livro = self.pesquisar_livro_por_id(livro_id)
        membro = self.pesquisar_membro_por_numero(numero_membro)

        if livro and membro and livro.status == 'Disponível':
            livro.status = 'Emprestado'
            membro.historico_emprestimos.append(livro)
            return True
        return False

    def devolver_livro(self, livro_id):
        livro = self.pesquisar_livro_por_id(livro_id)
        if livro and livro.status == 'Emprestado':
            livro.status = 'Disponível'
            return True
        return False

    def pesquisar_livro_por_id(self, livro_id):
        for livro in self.catalogo:
            if livro.id == livro_id:
                return livro
        return None

    def pesquisar_livro(self, termo):
        resultados = [livro for livro in self.catalogo if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower() or termo.lower() == str(livro.id)]
        return resultados

    def pesquisar_membro_por_numero(self, numero_membro):
        for membro in self.membros:
            if membro.numero_membro == numero_membro:
                return membro
        return None

    def pesquisar_membro(self, termo):
        resultados = [membro for membro in self.membros if termo.lower() in membro.nome.lower() or termo == membro.numero_membro]
        return resultados
