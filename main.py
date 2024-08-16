from classes import Biblioteca
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Funções da Interface
def adicionar_livro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    if titulo and autor:
        biblioteca.adicionar_livro(titulo, autor)
        atualizar_treeview_livros()
        entry_titulo.delete(0, tk.END)
        entry_autor.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Livro adicionado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Por favor, insira título e autor.")

def pesquisar_livro():
    termo = entry_pesquisa_livro.get()
    resultados = biblioteca.pesquisar_livro(termo)
    treeview_livros.delete(*treeview_livros.get_children())
    for livro in resultados:
        treeview_livros.insert("", "end", values=(livro.id, livro.titulo, livro.autor, livro.status))

def atualizar_treeview_livros():
    treeview_livros.delete(*treeview_livros.get_children())
    for livro in biblioteca.catalogo:
        treeview_livros.insert("", "end", values=(livro.id, livro.titulo, livro.autor, livro.status))

def cadastrar_membro():
    nome = entry_nome.get()
    numero_membro = entry_numero_membro.get()
    if nome and numero_membro:
        biblioteca.adicionar_membro(nome, numero_membro)
        atualizar_treeview_membros()
        entry_nome.delete(0, tk.END)
        entry_numero_membro.delete(0, tk.END)
        messagebox.showinfo("Sucesso", "Membro cadastrado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Por favor, insira nome e número de membro.")

def pesquisar_membro():
    termo = entry_pesquisa_membro.get()
    resultados = biblioteca.pesquisar_membro(termo)
    treeview_membros.delete(*treeview_membros.get_children())
    for membro in resultados:
        treeview_membros.insert("", "end", values=(membro.numero_membro, membro.nome))

def atualizar_treeview_membros():
    treeview_membros.delete(*treeview_membros.get_children())
    for membro in biblioteca.membros:
        treeview_membros.insert("", "end", values=(membro.numero_membro, membro.nome))

def emprestar_livro():
    livro_id = int(entry_livro_id_emprestar.get())
    numero_membro = entry_numero_membro_emprestar.get()
    if biblioteca.emprestar_livro(livro_id, numero_membro):
        atualizar_treeview_livros()
        messagebox.showinfo("Sucesso", "Livro emprestado com sucesso!")
    else:
        messagebox.showwarning("Erro", "Não foi possível emprestar o livro.")

def devolver_livro():
    livro_id = int(entry_livro_id_devolver.get())
    if biblioteca.devolver_livro(livro_id):
        atualizar_treeview_livros()
        messagebox.showinfo("Sucesso", "Livro devolvido com sucesso!")
    else:
        messagebox.showwarning("Erro", "Não foi possível devolver o livro.")

def consultar_historico_membro():
    numero_membro = entry_numero_membro_consultar.get()
    membro = biblioteca.pesquisar_membro_por_numero(numero_membro)
    if membro:
        historico = "\n".join([f"{livro.id} - {livro.titulo} ({livro.autor})" for livro in membro.historico_emprestimos])
        messagebox.showinfo("Histórico", f"Histórico de empréstimos de {membro.nome}:\n\n{historico}")
    else:
        messagebox.showwarning("Erro", "Membro não encontrado.")

# Inicializando a Biblioteca
biblioteca = Biblioteca()

# Interface Tkinter
root = tk.Tk()
root.title("Biblioteca")
root.geometry("1300x600")

# Frame superior para cadastro, empréstimo, devolução e histórico
frame_top = tk.Frame(root)
frame_top.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

# Frame inferior para a Treeview (lista de livros e membros)
frame_bottom = tk.Frame(root)
frame_bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=5, pady=5)

# Frame para cadastro de livros
frame_cadastro = tk.Frame(frame_top)
frame_cadastro.pack(side=tk.LEFT, padx=5)

tk.Label(frame_cadastro, text="Título do livro:").pack(anchor=tk.W)
entry_titulo = tk.Entry(frame_cadastro)
entry_titulo.pack(anchor=tk.W)

tk.Label(frame_cadastro, text="Autor do livro:").pack(anchor=tk.W)
entry_autor = tk.Entry(frame_cadastro)
entry_autor.pack(anchor=tk.W)

tk.Button(frame_cadastro, text="Adicionar Livro", command=adicionar_livro).pack(pady=5)

# Frame para cadastro de membros
frame_membro = tk.Frame(frame_top)
frame_membro.pack(side=tk.LEFT, padx=5)

tk.Label(frame_membro, text="Nome do Membro:").pack(anchor=tk.W)
entry_nome = tk.Entry(frame_membro)
entry_nome.pack(anchor=tk.W)

tk.Label(frame_membro, text="Número do Membro:").pack(anchor=tk.W)
entry_numero_membro = tk.Entry(frame_membro)
entry_numero_membro.pack(anchor=tk.W)

tk.Button(frame_membro, text="Cadastrar Membro", command=cadastrar_membro).pack(pady=5)

# Frame para empréstimo de livros
frame_emprestar = tk.Frame(frame_top)
frame_emprestar.pack(side=tk.LEFT, padx=5)

tk.Label(frame_emprestar, text="ID do Livro:").pack(anchor=tk.W)
entry_livro_id_emprestar = tk.Entry(frame_emprestar)
entry_livro_id_emprestar.pack(anchor=tk.W)

tk.Label(frame_emprestar, text="Número do Membro:").pack(anchor=tk.W)
entry_numero_membro_emprestar = tk.Entry(frame_emprestar)
entry_numero_membro_emprestar.pack(anchor=tk.W)

tk.Button(frame_emprestar, text="Emprestar Livro", command=emprestar_livro).pack(pady=5)

# Frame para devolução de livros
frame_devolver = tk.Frame(frame_top)
frame_devolver.pack(side=tk.LEFT, padx=5)

tk.Label(frame_devolver, text="ID do Livro:").pack(anchor=tk.W)
entry_livro_id_devolver = tk.Entry(frame_devolver)
entry_livro_id_devolver.pack(anchor=tk.W)

tk.Button(frame_devolver, text="Devolver Livro", command=devolver_livro).pack(pady=5)

# Frame para consultar histórico de membros
frame_historico = tk.Frame(frame_top)
frame_historico.pack(side=tk.LEFT, padx=5)

tk.Label(frame_historico, text="Número do Membro:").pack(anchor=tk.W)
entry_numero_membro_consultar = tk.Entry(frame_historico)
entry_numero_membro_consultar.pack(anchor=tk.W)

tk.Button(frame_historico, text="Consultar Histórico", command=consultar_historico_membro).pack(pady=5)

# Frames para Treeviews
frame_livros = tk.Frame(frame_bottom)
frame_livros.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

frame_membros = tk.Frame(frame_bottom)
frame_membros.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)

# Treeview para listar os livros
treeview_livros = ttk.Treeview(frame_livros, columns=("ID", "Título", "Autor", "Status"), show="headings")
treeview_livros.heading("ID", text="ID")
treeview_livros.heading("Título", text="Título")
treeview_livros.heading("Autor", text="Autor")
treeview_livros.heading("Status", text="Status")
treeview_livros.pack(fill=tk.BOTH, expand=True)

# Treeview para listar os membros
treeview_membros = ttk.Treeview(frame_membros, columns=("Número", "Nome"), show="headings")
treeview_membros.heading("Número", text="Número")
treeview_membros.heading("Nome", text="Nome")
treeview_membros.pack(fill=tk.BOTH, expand=True)

# Frame para pesquisa de membros
frame_pesquisa_membro = tk.Frame(frame_top)
frame_pesquisa_membro.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)

tk.Label(frame_pesquisa_membro, text="Pesquisar Membro:").pack(anchor=tk.W)
entry_pesquisa_membro = tk.Entry(frame_pesquisa_membro)
entry_pesquisa_membro.pack(anchor=tk.W)

tk.Button(frame_pesquisa_membro, text="Pesquisar", command=pesquisar_membro).pack(anchor=tk.W)

# Frame para pesquisa de livros
frame_pesquisa_livro = tk.Frame(frame_top)
frame_pesquisa_livro.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)

tk.Label(frame_pesquisa_livro, text="Pesquisar livro:").pack(anchor=tk.W)
entry_pesquisa_livro = tk.Entry(frame_pesquisa_livro)
entry_pesquisa_livro.pack(anchor=tk.W)

tk.Button(frame_pesquisa_livro, text="Pesquisar", command=pesquisar_livro).pack(anchor=tk.W)

# Frame para listar os membros e livros
frame_pesquisa_livro = tk.Frame(root)
frame_pesquisa_membro = tk.Frame(root)
frame_pesquisa_livro.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)
frame_pesquisa_membro.pack(side=tk.TOP, fill=tk.BOTH, padx=5, pady=5)

tk.Button(frame_pesquisa_livro, text="Todos os livros", command=atualizar_treeview_livros).pack(anchor=tk.W)
tk.Button(frame_pesquisa_membro, text="Todos os membros", command=atualizar_treeview_membros).pack(anchor=tk.E)


# Inicializar as listas
atualizar_treeview_livros()
atualizar_treeview_membros()

root.mainloop()
