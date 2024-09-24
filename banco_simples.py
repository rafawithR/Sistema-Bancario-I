from datetime import datetime as dt

hora = dt.now()

if hora.hour < 12:
    turno = 'Bom dia'
elif 12 <= hora.hour <= 18:
    turno = 'Boa tarde'
else:
    turno = 'Boa noite'

VALORES = ''
saldo: float = 0
LIMITE_VALOR_SAQUES: float = 500
LIMITE_DIARIO_SAQUES = 0

def saque(quantia):
    global VALORES
    global saldo
    saldo -= quantia
    VALORES += f'Saque    {hora.month}/{hora.year} -R${quantia:.2f}\n'
    return saldo

def deposito(quantia):
    global VALORES
    global saldo
    saldo += quantia
    VALORES += f'Deposito {hora.month}/{hora.year}  R${quantia:.2f}\n'
    return saldo

while True:
    print(f'''
################################# MENU ##################################

Data: {hora.day}/{hora.month}/{hora.year}  
Hora{hora.ctime()[10:16]}

{turno}! O que você gostaria de fazer?

        [1] - Sacar 
        [2] - Depositar
        [3] - Verificar extrato bancário
        [0] - Sair do sistema

        ''')
    opcao = input('O que você deseja fazer: ')

    if int(opcao) == 1:
        quantia = float(input("Quanto você deseja sacar? "))
        if (float(quantia) >= LIMITE_VALOR_SAQUES):
            print('O valor máximo por saque é de R$500.')
        elif LIMITE_DIARIO_SAQUES >= 3:
            print('Limite de 3 saques diários já atingidos.')
        elif (float(quantia) > saldo) :
            print(f'Saldo insuficiente! Seu saldo atual é R${saldo:.2f}.')
        elif quantia <= 0:
            print(f'Valor incorreto informado.')
        else:
            saque(quantia)
            LIMITE_DIARIO_SAQUES += 1
            print(f'''
Saque realizado com sucesso!
            
Seu saldo atual é R${saldo:.2f}.
''')

    elif int(opcao) == 2:
        quantia = float(input('Quanto você gostaria de depositar? '))
        if quantia <= 0:
            print(f'Valor incorreto informado.')
        else:
            deposito(quantia)
            print(f'''
Deposito realizado com sucesso!

Seu saldo atual é R${saldo:.2f}
''')
    elif int(opcao) == 3:
            print('EXTRATO'.center(29, '-'))
            print(f'Não há registros de movimentação na sua conta' if not VALORES else VALORES)
            print(f'''Seu saldo atual é {saldo:.2f}
------------------------------''')
    elif int(opcao) == 0:
        print(f'''

Obrigado por escolher nosso banco! {turno} e volte sempre!

''')
        break
    else:
        print('Opção inválida')