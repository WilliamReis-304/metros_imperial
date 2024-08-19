class Elevador:
    def __init__(self, totalCapacidade, totalAndar):
        self.totalCapacidade = totalCapacidade  # Capacidade máxima do elevador
        self.atualCapacidade = 0  # Capacidade atual do elevador (inicialmente vazio)
        self.totalAndar = totalAndar  # Total de andares do prédio
        self.atualAndar = 0  # Andar atual do elevador (inicialmente no térreo)

    def Subir(self):
        if self.atualAndar < self.totalAndar - 1:  # Verifica se não está no último andar
            self.atualAndar += 1
            print(f"Subindo para o andar {self.atualAndar}")
        else:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")

    def Descer(self):
        if self.atualAndar > 0:  # Verifica se não está no térreo
            self.atualAndar -= 1
            print(f"Descendo para o andar {self.atualAndar}")
        else:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")

    def Entrar(self):
        if self.atualCapacidade < self.totalCapacidade:  # Verifica se não está cheio
            self.atualCapacidade += 1
            print(f"Entrando uma pessoa. Capacidade atual: {self.atualCapacidade}/{self.totalCapacidade}")
        else:
            print("O ELEVADOR ESTÁ CHEIO!")

    def Sair(self):
        if self.atualCapacidade > 0:  # Verifica se há alguém no elevador
            self.atualCapacidade -= 1
            print(f"Saindo uma pessoa. Capacidade atual: {self.atualCapacidade}/{self.totalCapacidade}")
        else:
            print("NÃO TEM NINGUÉM.")




