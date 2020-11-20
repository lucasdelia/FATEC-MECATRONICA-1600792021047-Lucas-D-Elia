import random
repeticao = 0
senha_ID1 = 'lucas123'
senha_ID2 = 'qualquer_bosta'
senha_ID3 = 'senha'
saldo_atualID1 = 1000.00
saldo_atualID2 = 250.00
saldo_atualID3 = 3000.00
email1 = 'lucasdelia2014@hotmail.com'
email2 = 'rafaelmendes_barros@hotmail.com'
email3 = 'murilo.zcarvalho@fatec.sp.gov.br'
resposta = 'Sim'
resposta1 = 'sim'
resposta2 = 'sim'
resposta3 = 'sim'
resposta4 = 'sim'
ID1 = senha_ID1
ID2 = senha_ID2
ID3 = senha_ID3
Sim = True
while resposta == 'Sim':
  while resposta1 == 'sim':
    print('Pagamento de Rafao de R$250,00 para Geleia')
    print('Faça login com a conta de Rafao e faça a transação para Geleia')
    print('ID1 é a usuária Geleia')
    print('ID2 é o usuário Rafao')
    print('ID3 é o usuário Murilo')
    usuario = input('Usuario: ')
    senha = input('Senha: ')
    email2 = input('E-mail: ')
    if usuario == 'Rafao' and senha == senha_ID2 and email2 == 'rafaelmendes_barros@hotmail.com':
         print(f'Seu saldo atual é de R${saldo_atualID2: .2f}')
         recebedor = input('Informe o nome do recebedor do pagamento: ')
         if recebedor == 'Geleia':
           valor_pagamento = float(input('Informe o valor da transação: '))
           if saldo_atualID2 >= valor_pagamento:
             pagamento = (saldo_atualID2 - valor_pagamento)
             saldo_atualID2 = (saldo_atualID2 - valor_pagamento)
             saldo_atualID1 = (saldo_atualID1 + valor_pagamento)
             print('Transação realizada com sucesso')
             print('Transação realizada por:', usuario)
             print('Transação realizada para:', recebedor)
             print(f'Valor da transação R${valor_pagamento: .2f}')
             print("Sua chave de segurança é:"),print(random.randrange(1000, 9999))
             print('Email: ',email2)
             print(f'Saldo atual de Geleia é de R${saldo_atualID1: .2f}')
             print(f'Saldo atual de Rafao é de R${saldo_atualID2: .2f}')
             print(f'Saldo atual de Murilo é de R${saldo_atualID3: .2f}')
           elif saldo_atualID2 < valor_pagamento:
             print('Você não tem saldo o suficiente para realizar a transação')
             saldo_atualID1 = saldo_atualID1
             saldo_atualID2 = saldo_atualID2
    else:
        print('Usuário ou Senha incorreto')
    resposta1 = input('Deseja repetir a operação? (sim ou não) ')
  while resposta2 == 'sim':
    print('Geleia gera uma operação de recebimento de R$ 250.00 para o Murilo')
    print('Faça login com a conta de Murilo e faça a transação para Geleia')
    print('ID1 é a usuária Geleia')
    print('ID2 é o usuário Rafao')
    print('ID3 é o usuário Murilo')
    usuario = input('Informe o seu nome de Usuário: ')
    senha = input('Informe a sua senha: ')
    email3 = input('Informe o seu e-mail: ')
    if usuario == 'Murilo' and senha == senha_ID3 and email3 == 'murilo.zcarvalho@fatec.sp.gov.br':
      if senha == senha_ID3:
        print('Seu saldo atual é de R$', saldo_atualID3)
        recebedor = input('Informe o nome do recebedor do pagamento: ')
        if recebedor == 'Geleia':
          valor_pagamento = float(input('Informe o valor da transação: '))
          if saldo_atualID3 >= valor_pagamento:
            pagamento = (saldo_atualID3 - valor_pagamento)
            saldo_atualID3 = (saldo_atualID3 - valor_pagamento)
            saldo_atualID1 = (saldo_atualID1 + valor_pagamento)
            print('Transação realizada com sucesso')
            print('Transação realizada por:', usuario)
            print('Transação realizada para:', recebedor)
            print(f'Valor da transação R${valor_pagamento: .2f}')
            print("Sua chave de segurança é:"),print(random.randrange(1000, 9999))
            print('Email: ',email3)
            print(f'Saldo atual de Geleia é de R${saldo_atualID1: .2f}')
            print(f'Saldo atual de Rafao é de R${saldo_atualID2: .2f}')
            print(f'Saldo atual de Murilo é de R${saldo_atualID3: .2f}')
          elif saldo_atualID3 < valor_pagamento:
            print('Você não tem saldo o suficiente para realizar a transação')
            saldo_atualID3 = saldo_atualID3
            saldo_atualID1 = saldo_atualID1
    else:
        print('Usuário ou Senha incorreto')
    resposta2 = input('Deseja repetir a operação? (sim ou não) ')
  while resposta3 == 'sim':
    print('Geleia gera uma operação de recebimento de R$ 250.00 para o Rafao')
    print('Faça login com a conta de Rafao e faça a transação para Geleia')
    print('ID1 é a usuária Geleia')
    print('ID2 é o usuário Rafao')
    print('ID3 é o usuário Murilo')
    usuario = input('Informe o seu nome de Usuário: ')
    senha = input('Informe a sua senha: ')
    email2 = input('Informe o seu e-mail: ')
    if usuario == 'Rafao' and senha == senha_ID2 and email2 == 'rafaelmendes_barros@hotmail.com':
        print(f'Seu saldo atual é de R$ {saldo_atualID2: .2f}')
        recebedor = input('Informe o nome do recebedor do pagamento: ')
        if recebedor == 'Geleia':
          valor_pagamento = float(input('Informe o valor da transação: '))
          if saldo_atualID2 >= valor_pagamento:
            pagamento = (saldo_atualID2 - valor_pagamento)
            saldo_atualID1 = (saldo_atualID1 + valor_pagamento)
            saldo_atualID2 = (saldo_atualID2 - valor_pagamento)
            print('Transação realizada com sucesso')
            print('Transação realizada por:', usuario)
            print('Transação realizada para:', recebedor)
            print(f'Valor da transação R${valor_pagamento: .2f}')
            print("Sua chave de segurança é:"),print(random.randrange(1000, 9999))
            print('Email: ',email2)
            print(f'Saldo atual de Geleia é de R${saldo_atualID1: .2f}')
            print(f'Saldo atual de Rafao é de R${saldo_atualID2: .2f}')
            print(f'Saldo atual de Murilo é de R${saldo_atualID3: .2f}')
          elif saldo_atualID2 < valor_pagamento:
            print('Você não tem saldo o suficiente para realizar a transação')
            saldo_atualID1 = saldo_atualID1
            saldo_atualID2 = saldo_atualID2
            print(saldo_atualID1)
            print(saldo_atualID2)
            print(saldo_atualID3)
    else:
        print('Usuário ou Senha incorreto')
    resposta3 = input('Deseja repetir a operação? (sim ou não) ')
  while resposta4 == 'sim':
    print('Rafao gera uma operação de recebimento de R$ 1000.00 para o Murilo')
    print('Faça login com a conta de Murilo e faça a transação para Rafao')
    print('ID1 é a usuária Geleia')
    print('ID2 é o usuário Rafao')
    print('ID3 é o usuário Murilo')
    usuario = input('Informe o seu nome de Usuário: ')
    senha = input('Informe a sua senha: ')
    email3 = input('Informe o seu e-mail: ')
    if usuario == 'Murilo' and senha == senha_ID3 and email3 == 'murilo.zcarvalho@fatec.sp.gov.br':
        print('Seu saldo atual é de R$', saldo_atualID3)
        recebedor = input('Informe o nome do recebedor do pagamento: ')
        if recebedor == 'Rafao':
          valor_pagamento = float(input('Informe o valor da transação: '))
          if saldo_atualID3 >= valor_pagamento:
            pagamento = (saldo_atualID3 - valor_pagamento)
            saldo_atualID3 = (saldo_atualID3 - valor_pagamento)
            saldo_atualID2 = (saldo_atualID2 + valor_pagamento)
            print('Transação realizada com sucesso')
            print('Transação realizada por:', usuario)
            print('Transação realizada para:', recebedor)
            print(f'Valor da transação R${valor_pagamento: .2f}')
            print("Sua chave de segurança é:"),print(random.randrange(1000, 9999))
            print('Email: ',email3)
            print(f'Saldo atual de Geleia é de R${saldo_atualID1: .2f}')
            print(f'Saldo atual de Rafao é de R${saldo_atualID2: .2f}')
            print(f'Saldo atual de Murilo é de R${saldo_atualID3: .2f}')
          elif saldo_atualID3 < valor_pagamento:
            print('Você não tem saldo o suficiente para realizar a transação')
            saldo_atualID3 = saldo_atualID3
            saldo_atualID2 = saldo_atualID2
    else:
        print('Usuário ou Senha incorreto')
    resposta4 = input('Deseja repetir a operação? (sim ou não) ')
resposta = ('Deseja repetir as operações? (Sim ou Não)')
print('Fim do programa')
