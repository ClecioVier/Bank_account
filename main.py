from Orientação_ao_objeto_contabanco import ContaCorrente, CartaoCredito

# programa

conta_001 = ContaCorrente("João", "000.000.111-78", 1234, 456789)

conta_001.consultar_saldo()

# depositar dinheiro
conta_001.depositar(10000)

# sacar dinheiro
conta_001.sacar(2500)

conta_001.consultar_saldo()

conta_001.consultar_limite()

# Consultar historico
conta_001.consultar_historico_transacoes()

# Fazer transferencia
conta_002 = ContaCorrente('Jose', '321.313.123-99', 1111, 122122)
conta_001.transferir(100, conta_002)

conta_001.consultar_saldo()
conta_002.consultar_saldo()

#Criar cartão de crédito
cartao_conta_001 = CartaoCredito('Jose', conta_001)

#Consultar dados do cartao

print(cartao_conta_001.cod_seguranca)
print(cartao_conta_001.validade)

#trocar senha

cartao_conta_001.senha = '2345'
print(cartao_conta_001.senha)


#consultar dicionários
print(conta_001.__dict__)