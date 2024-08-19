from classes import *

tipoCombustivel = input("Digite o tipo de combustível (ex: Gasolina, Diesel): ")
valorLitro = float(input("Digite o valor por litro do combustível: "))
quantidadeCombustivel = float(input("Digite a quantidade de combustível na bomba (em litros): "))

bomba = bombaCombustivel(tipoCombustivel, valorLitro, quantidadeCombustivel)

while True:
    print("\n--- Menu da Bomba de Combustível ---")
    print("1. Abastecer por valor")
    print("2. Abastecer por litro")
    print("3. Alterar valor do litro")
    print("4. Alterar tipo de combustível")
    print("5. Alterar quantidade de combustível na bomba")
    print("6. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        valor = float(input("Digite o valor a ser abastecido: R$"))
        bomba.abastecerPorValor(valor)
    elif opcao == "2":
        litros = float(input("Digite a quantidade de litros a ser abastecida: "))
        bomba.abastecerPorLitro(litros)
    elif opcao == "3":
        novo_valor = float(input("Digite o novo valor por litro do combustível: R$"))
        bomba.alterarValor(novo_valor)
    elif opcao == "4":
        novo_tipo = input("Digite o novo tipo de combustível: ")
        bomba.alterarCombustivel(novo_tipo)
    elif opcao == "5":
        nova_quantidade = float(input("Digite a nova quantidade de combustível na bomba (em litros): "))
        bomba.alterarQuantidadeCombustivel(nova_quantidade)
    elif opcao == "6":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha novamente.")