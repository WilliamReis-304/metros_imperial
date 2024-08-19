import os

# Lista dfeita para armazenar as tarefas
tarefas = []

# Função para adicionar uma tarefa
def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa '{nome}' adicionada com sucesso.")

# Função para listar todas as tarefas
def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        for i, tarefa in enumerate(tarefas):
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{i+1}. {tarefa['nome']} - {tarefa['descricao']} [Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Status: {status}]")

# Função para marcar uma tarefa como concluída
def concluir_tarefa(indice):
    try:
        tarefas[indice]["concluida"] = True
        print(f"Tarefa '{tarefas[indice]['nome']}' marcada como concluída.")
    except IndexError:
        print("Índice de tarefa inválido.")

# Função para exibir tarefas por prioridade
def listar_por_prioridade(prioridade):
    filtradas = [tarefa for tarefa in tarefas if tarefa["prioridade"] == prioridade]
    if filtradas:
        for tarefa in filtradas:
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{tarefa['nome']} - {tarefa['descricao']} [Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Status: {status}]")
    else:
        print(f"Nenhuma tarefa encontrada com prioridade {prioridade}.")

# Função para exibir tarefas por categoria
def listar_por_categoria(categoria):
    filtradas = [tarefa for tarefa in tarefas if tarefa["categoria"] == categoria]
    if filtradas:
        for tarefa in filtradas:
            status = "Concluída" if tarefa["concluida"] else "Pendente"
            print(f"{tarefa['nome']} - {tarefa['descricao']} [Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Status: {status}]")
    else:
        print(f"Nenhuma tarefa encontrada na categoria {categoria}.")

# Função para exibir o menu de comandos
def exibir_menu():
    print("\nGerenciador de Tarefas")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Marcar Tarefa como Concluída")
    print("4. Listar Tarefas por Prioridade")
    print("5. Listar Tarefas por Categoria")
    print("6. Sair")
