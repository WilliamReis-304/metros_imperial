class bombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel  # Tipo de combustível (ex: Gasolina, Diesel)
        self.valorLitro = valorLitro  # Valor por litro do combustível
        self.quantidadeCombustivel = quantidadeCombustivel  # Quantidade de combustível na bomba (em litros)

    def abastecerPorValor(self, valor):
        litros_abastecidos = valor / self.valorLitro  # Calcula a quantidade de litros abastecidos
        if litros_abastecidos <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros_abastecidos  # Atualiza a quantidade de combustível na bomba
            print(f"Abastecido {litros_abastecidos:.2f} litros de {self.tipoCombustivel}.")
            print(f"Quantidade restante na bomba: {self.quantidadeCombustivel:.2f} litros.")
        else:
            print("Quantidade de combustível insuficiente na bomba para abastecer esse valor.")
    
    def abastecerPorLitro(self, litros):
        valor_a_pagar = litros * self.valorLitro  # Calcula o valor a ser pago pelo cliente
        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros  # Atualiza a quantidade de combustível na bomba
            print(f"O valor a ser pago por {litros:.2f} litros de {self.tipoCombustivel} é R${valor_a_pagar:.2f}.")
            print(f"Quantidade restante na bomba: {self.quantidadeCombustivel:.2f} litros.")
        else:
            print("Quantidade de combustível insuficiente na bomba para abastecer essa quantidade de litros.")
    
    def alterarValor(self, novo_valor):
        self.valorLitro = novo_valor  # Altera o valor do litro do combustível
        print(f"O novo valor do litro de {self.tipoCombustivel} é R${self.valorLitro:.2f}.")
    
    def alterarCombustivel(self, novo_tipo):
        self.tipoCombustivel = novo_tipo  # Altera o tipo de combustível
        print(f"O tipo de combustível foi alterado para {self.tipoCombustivel}.")
    
    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidadeCombustivel = nova_quantidade  # Altera a quantidade de combustível restante na bomba
        print(f"A quantidade de combustível na bomba foi atualizada para {self.quantidadeCombustivel:.2f} litros.")

