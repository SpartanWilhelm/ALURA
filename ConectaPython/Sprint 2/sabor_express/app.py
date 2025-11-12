import os

restaurantes = ['Pizza Hut', 'McDonalds', 'Giraffas']

def finalizar_app() :
    exibir_subtitulo('Finalizar app')

def opcao_invalida():
    print('Opção inválida.\n')    
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(f'{texto}\n')

def voltar_ao_menu_principal():    
    input('\nDigite uma tecla para voltar ao menu')
    os.system('cls')
    main()

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

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso\n')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes cadastrados')
    for restaurante in restaurantes:
        print(f'. {restaurante}')
    voltar_ao_menu_principal()

def ativar_restaurante():
    exibir_subtitulo('Ativando um restaurante')
    pass

def escolher_opcao():
    try:
        opcao_escolhida = input('Digite a opção escolhida: ')
        print(f'Você escolheu a opção {opcao_escolhida}')
        if opcao_escolhida == '1':
            cadastrar_novo_restaurante()
        elif opcao_escolhida == '2':
            listar_restaurantes()
        elif opcao_escolhida == '3':
            ativar_restaurante()
        elif opcao_escolhida == '4':
            finalizar_app()
        else:    
            opcao_invalida()
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()