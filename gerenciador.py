from funcoes import *

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Nome da Tarefa: ")
        descricao = input("Descrição da Tarefa: ")
        prioridade = input("Prioridade (Alta, Média, Baixa): ")
        categoria = input("Categoria da Tarefa: ")
        adicionar_tarefa(nome, descricao, prioridade, categoria)
    
    elif opcao == "2":
        listar_tarefas()
    
    elif opcao == "3":
        listar_tarefas()
        indice = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
        concluir_tarefa(indice)
    
    elif opcao == "4":
        prioridade = input("Digite a prioridade (Alta, Média, Baixa): ")
        listar_por_prioridade(prioridade)
    
    elif opcao == "5":
        categoria = input("Digite a categoria: ")
        listar_por_categoria(categoria)
    
    elif opcao == "6":
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
