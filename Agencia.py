from random import randint


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nivel recomendado. Caixa atual: R${:,.2f}'.format(self.caixa))
        else:
            print('Caixa atual está ok. Caixa atual: R${:,.2f}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Emprestimo não autorizado, caixa insuficiente')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000)
        self.caixa = 1000000
        self.caixa_paypal = 0

    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor

    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor

class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj, numero):
        super().__init__(telefone, cnpj, numero=randint(2000, 9999))
        self.caixa = 1000000

class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj, numero):
        super().__init__(telefone, cnpj, numero=randint(2000, 9999))
        self.caixa = 10000000

    def adicionar_cliente(self, nome, cpf, patrimonio):
        if patrimonio > 1000000:
            super().adicionar_cliente(nome, cpf, patrimonio)
        else:
            print('O cliente não possui patrimonio necessário para abertura da conta')



agencia1 = Agencia(35236655, 1225412000189, 1452)

agencia1.caixa = 2500000

#consultar caixa da agencia:
agencia1.verificar_caixa()

#Realizar emprestimo:
agencia1.emprestar_dinheiro(2000, 12365478, 0.01)
print(agencia1.emprestimos)

#Adicionar clientes:
agencia1.adicionar_cliente('Cleber', 12365478, 10000)
print(agencia1.clientes)

#Criar agencia virtual:

agencia_virtual = AgenciaVirtual(35221478, 236547896663, 4569)
print(agencia_virtual)
agencia_virtual.caixa = 500000
agencia_virtual.verificar_caixa()

#Criar agencia premium:
agencia_premium = AgenciaPremium(35214789, 25100000000, 7896)
agencia_premium.caixa = 5000000000
agencia_premium.verificar_caixa()

#Depositar paypal
agencia_virtual.depositar_paypal(100000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)

#Adicionar cliente premium
agencia_premium.adicionar_cliente('cesar', 3334444890, 1000001)