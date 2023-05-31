saldo = 1000
LIMITE_SAQUE = 0
VALOR_MAXIMO = 500
extrato_saque = []
extrato_deposito = []

while True:
    print('-'*80)
    print('Desafio DIO - Sistema Bancário'.center(80))
    print('-'*80)
    opt = input(
        '''
        Seja bem vindo, selecione uma opção:
        1 - Depositar
        2 - Saque
        3 - Extrato
        0 - Sair do app
        ''')

    if opt == '1':
        dep = float(input('Insira o valor de depósito: '))
        if dep < 0:
            print('Valor inválido, tente novamente.')
        else:
            extrato_deposito.append(dep)
            saldo += dep
            print('Processo concluído !')
            
            
    elif opt == '2':
        if LIMITE_SAQUE >= 3:
            print('Esta operação não pode ser realizada')
            print('Limites de saques atingidos')
        else:
            saque = float(input('Insira o valor para saque: '))
            if saque > VALOR_MAXIMO:
                print(f'Valor maximo ultrapassado (R$ {VALOR_MAXIMO})')
            elif (saldo - saque) < 0:
                print('Saldo insuficiente')
            else:
                extrato_saque.append(saque)
                saldo -= saque
                LIMITE_SAQUE += 1
                print('Operação realizada')
            
    elif opt == '3':
        print('DEPÓSITOS'.center(80))
        if extrato_deposito == []:
                print('Não houve movimentação') 
        else:
            for a in extrato_deposito:
                print(f'Depósito R$ {a:.2f}')
            
            
        print('SAQUES'.center(80))
        if extrato_saque == []:
            print('Não houve movimentação')
        else:
            for a in extrato_saque:
                print(f'Saque R$ {a:.2f}')
    
    elif opt == '0':
        print('Encerando APP'.center(80))
        print('-'*80)
        break
    else:
        print('Opção inválida, tente novamente')    
    
 
    print(f'\nSaldo atual R$ {saldo}')
