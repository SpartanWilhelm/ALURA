import os

def finalizar_app() :
    os.system('cls')
    print('Finalizando o app\n')

def exibir_nome_do_programa():
    print ("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")
    
def exibir_opcoes():    
    print ('1 - Cadastrar Restaurante')
    print ('2 - Listar Restaurante')
    print ('3 - Ativar Restaurante')
    print ('4 - Sair\n')

def escolher_opcao():
    opcao_escolhida = input('Digite a opção escolhida: ')
    print(f'Você escolheu a opção {opcao_escolhida}')
    if opcao_escolhida == '1':
        print('Cadastrar Restaurante')
    elif opcao_escolhida == '2':
        print('Listar Restaurante')
    elif opcao_escolhida == '3':
        print('Ativar Restaurante')
    else:    
        finalizar_app()


def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()