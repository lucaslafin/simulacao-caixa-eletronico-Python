import os
import time

banco = []

# Interface inicial
def interface():
    os.system('cls')
    print('|Santander|\n\nCaso queira criar um cadastro aperte [1]\nJá possui conta? aperte [2]')
    opcao_escolhida = input('')
    
    if opcao_escolhida == '1':
        cadastro()
        
    elif opcao_escolhida == '2':
        autenticar()
          
    else:
        opcao_invalida()

# Voltar ao menu inicial            
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

# Para caso o usuário escolha uma opção errada
def opcao_invalida():
    os.system('cls')
    print('Opção inválida!\n')
    voltar_ao_menu_principal()        

# Criação do cadastro   
def cadastro():
    os.system('cls')
    nome_cadastrado = input('Digite seu nome: ')
    senha_cadastrada = input('Digite sua senha: ')
    dados_dos_clientes = {'nome': nome_cadastrado, 'senha': senha_cadastrada, 'saldo': 0, 'transacoes': [],'ativo': True}
    banco.append(dados_dos_clientes)
    print('Seu cadastro foi concluído com sucesso!!!')
    voltar_ao_menu_principal()

# Login
def autenticar():
    os.system('cls')
    usuario_input = input("Digite seu nome de usuário: ")
    usuario_encontrado = False

    for cliente in banco:
        if cliente['nome'] == usuario_input:
            usuario_encontrado = True
            if cliente['ativo'] == True:
                for tentativa in range(3):
                    senha_input = input("Digite sua senha: ")
                    if senha_input == cliente['senha']:
                        interface_da_conta(cliente)
                        return
                    else:
                        print(f"Senha incorreta! Você tem {2 - tentativa} tentativas restantes.")
                print("Número máximo de tentativas atingido!")
                cliente['ativo'] = not cliente['ativo']
                voltar_ao_menu_principal()
                return
            else:
                print("Sua conta está bloqueada! Vá ao caixa mais proximo para desbloquear sua conta!")
                voltar_ao_menu_principal()
                return
    if not usuario_encontrado:
        print("Usuário não encontrado!")
        voltar_ao_menu_principal()
        
# Interface da conta
def interface_da_conta(cliente):
    os.system('cls')
    print("Aguarde enquanto estamos abrindo sua conta ツ")
    time.sleep(2)
    os.system('cls')
    print(f'Bem vindo {cliente['nome']}\n[1] Realizar depósitos\n[2] Saques\n[3] Transferência\n[4] Consultar extrato da conta\n[5] Sair')
    selecionar_opcao = input('Digite como deseja prosseguir: ')
        
    if selecionar_opcao == '1':
        os.system('cls')
        depositos(cliente)
    elif selecionar_opcao == '2':
        os.system('cls')
        saques(cliente)
    elif selecionar_opcao == '3':
        os.system('cls')    
        transferencias(cliente)
    elif selecionar_opcao == '4':
        os.system('cls')
        consultar_extrato(cliente)   
    elif selecionar_opcao == '5':
        os.system('cls')
        voltar_ao_menu_principal()   
    else:
        print('\nOpção inválida, atualizando a página...')
        time.sleep(2)
        interface_da_conta(cliente)

# Função para depósitos
def depositos(cliente):
    os.system('cls')
    print('Digite abaixo o valor que deseja depositar na conta:')
    valor_cadastrado = float(input(''))
    cliente['saldo'] += valor_cadastrado
    cliente['transacoes'].append(f'Depósito: R$ {valor_cadastrado:.2f}')
    print(f'O valor de R$ {valor_cadastrado:.2f} foi adicionado à sua conta!!!')
    input('Digite uma tecla para voltar')
    interface_da_conta(cliente)

# Função para saques
def saques(cliente):
    os.system('cls')
    print('Digite abaixo o valor que deseja sacar da conta:')
    valor_sacado = float(input(':'))

    for tentativa in range(3):
        senha_input = input("Digite sua senha para confirmar o saque: ")
        if senha_input == cliente['senha']:
            if valor_sacado > cliente['saldo']:
                print("Saldo insuficiente!")
            else:
                cliente['saldo'] -= valor_sacado
                cliente['transacoes'].append(f'Saque: R$ {valor_sacado:.2f}')
                print(f'O valor de R$ {valor_sacado:.2f} foi retirado da sua conta.')
                input('Digite uma tecla para voltar')
                interface_da_conta(cliente)
            break
        else:
            print(f"Senha incorreta! Você tem {2 - tentativa} tentativas restantes.")
    else:
        print("Número máximo de tentativas atingido, vá ao caixa mais proximo para desbloquear sua conta!")
        cliente['ativo'] = not cliente['ativo']
        voltar_ao_menu_principal()

# Função para transferências
def transferencias(cliente):
    os.system('cls')
    nome_destinado = input('Digite o nome do destinatário: ')
    valor_transferencia = float(input('Digite o valor a ser transferido: '))
    destinatario_encontrado = False
    
    for conta in banco:
        if conta['nome'] == nome_destinado:
            destinatario_encontrado = True
            break

    if not destinatario_encontrado:
        print('Destinatário não encontrado!')
        input('Digite uma tecla para voltar')
        interface_da_conta(cliente)
        return

    for tentativa in range(3):
        senha_da_conta = input('Digite sua senha: ')
        if senha_da_conta == cliente['senha']:
            if valor_transferencia > cliente['saldo']:
                print("Saldo insuficiente para transferência!")
            else:
                cliente['saldo'] -= valor_transferencia
                conta['saldo'] += valor_transferencia
                cliente['transacoes'].append(f'Transferência: R$ {valor_transferencia:.2f} para {nome_destinado}')
                conta['transacoes'].append(f'Transferência: R$ {valor_transferencia:.2f} recebida de {cliente["nome"]}')
                print(f'R$ {valor_transferencia:.2f} transferido para {nome_destinado} com sucesso!')
                input('\ndigite uma tecla para voltar')
                interface_da_conta(cliente)
            break
        else:
            print(f'Senha incorreta! Você tem {2 - tentativa} tentativas restantes.')
    else:
        print('Número máximo de tentativas atingido , vá ao caixa mais proximo para desbloquear sua conta!')
        cliente['ativo'] = not cliente['ativo']
        input('\nDigite uma tecla para voltar')
        voltar_ao_menu_principal()
        
# Função para consultar extrato
def consultar_extrato(cliente):
    os.system('cls')
    saldo = cliente['saldo']
    transacoes = "\n".join(cliente['transacoes']) if cliente['transacoes'] else 'Nenhuma transação realizada.'
    print(f'Saldo: R$ {saldo:.2f}\n\n{transacoes}"]')
    input('Digite uma tecla para voltar')
    interface_da_conta(cliente)

def main():
    os.system('cls')
    interface()

if __name__ == '__main__':
    main()
