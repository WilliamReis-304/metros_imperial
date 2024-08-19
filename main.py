from classes import *

totalCapacidade = int(input("Digite a capacidade máxima do elevador: "))
totalAndar = int(input("Digite o total de andares do prédio: "))
elevador = Elevador(totalCapacidade, totalAndar)
print("Elevador configurado!")

while True:
    print("\n--- Menu do Elevador ---")
    print("1. Subir")
    print("2. Descer")
    print("3. Entrar")
    print("4. Sair")
    print("5. Sair do Programa")
    
    opcao = input("\nEscolha uma opção:\n")
    
    if opcao == "1":
        elevador.Subir()
    elif opcao == "2":
        elevador.Descer()
    elif opcao == "3":
        elevador.Entrar()
    elif opcao == "4":
        elevador.Sair()
    elif opcao == "5":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.\n")
