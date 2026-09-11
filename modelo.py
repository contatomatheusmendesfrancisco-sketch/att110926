class Conta:
    TAXA_SERVICO = 0.10
    def __init__(self):
        self.valor = 0
        self.comanda = []
        self.porPessoa = 0
        self.qtdPessoas = 0
        self.valorServico = 0

    def adicionar(self, nome, valor):
        self.comanda.append([nome, valor])
        self.qtdPessoas += 1

    def total_pessoas(self):
        return self.qtdPessoas

    def subtotal(self):
        calculado = 0
        for item in self.comanda:
            calculado += int(item[1])
        self.valor = calculado
        return self.valor

    def valor_servico(self):
        self.valorServico = self.subtotal() * self.TAXA_SERVICO
        return self.valorServico

    def total(self):
        self.valor = self.subtotal() + self.valorServico
        return self.valor

    def por_pessoa(self):
        if self.qtdPessoas == 0:
            return 0.0
        self.porPessoa = self.valor / self.qtdPessoas
        return self.porPessoa

    def listar(self):
        return self.comanda

    def esvaziar_conta(self):
        self.__init__()


#arduino is my bags
