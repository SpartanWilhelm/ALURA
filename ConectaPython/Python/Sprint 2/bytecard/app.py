import os
import json

compra = []


def exibir_nome_do_programa():
    print('ByteCard 1.0')

def voltar_ao_menu_principal():  
    input('\nDigite uma tecla para voltar ao menu')  
    os.system('cls')
    main()

def exibir_opcoes():
    print('1 - Nova compra')
    print('2 - Listar Compras')
    print('3 - Cancelar Compra')
    print('4 - Calcular Total Gasto')
    print('5 - Relatório de gastos por categoria')
    print('99 - Sair\n')

def opcao_invalida():
    print('Opção inválida.\n')    
    voltar_ao_menu_principal()

def nova_compra():
    cartao = input('Digite o número do cartão: ')
    valor = input('Digite o valor da compra: ')
    data = input('Digite a data da compra (dd/mm/aaaa): ')
    cliente = input('Digite o nome do cliente: ')
    categoria = input('Digite a categoria da compra: ')
    nova_compra = {'cartao': cartao, 'valor': valor, 'data': data, 'cliente': cliente, 'categoria': categoria}
    compra.append(nova_compra)
    salvar_dados_em_arquivo()
    print('Compra cadastrada com sucesso!\n')
    voltar_ao_menu_principal()

def listar_compras():
    ler_dados_de_arquivo()
    print('Listando todas as compras cadastradas:\n')
    print(f'{"Cartão".ljust(12)} | {"Valor".ljust(12)} | {"Data".ljust(10)} | {"Cliente".ljust(10)} | {"Categoria"}')
    for compra_item in compra:
        cartao = compra_item['cartao']
        valor = compra_item['valor']
        data = compra_item['data']
        cliente = compra_item['cliente']
        categoria = compra_item['categoria']
        print(f'. {cartao.ljust(10)} | {valor.ljust(10)} | {data.ljust(12)} | {cliente.ljust(15)} | {categoria}')
    voltar_ao_menu_principal()

def cancelar_compra():
    ler_dados_de_arquivo()
    cartao = input('Digite o número do cartão da compra que deseja cancelar: ')
    valor = input(f'Digite o valor da compra que deseja  cancelar no cartão {cartao}: ')
    compra_encontrada = False
    for compra_item in compra:
        if compra_item['cartao'] == cartao and compra_item['valor'] == valor:
            compra.remove(compra_item)
            compra_encontrada = True
            salvar_dados_em_arquivo()
            print('Compra cancelada com sucesso!\n')
            break
    if not compra_encontrada:
        print(f'Compra no valor de {valor} no cartão {cartao} não localizada.\n')
    voltar_ao_menu_principal()

def calcular_total_gasto():
    ler_dados_de_arquivo()
    cartao = input('Digite o número do cartão para calcular o total gasto: ')
    total_gasto = 0
    for compra_item in compra:
        if compra_item['cartao'] == cartao:
            total_gasto += float(compra_item['valor'])
    if total_gasto != 0:
        print(f'O total gasto no cartão {cartao} é: R$ {total_gasto:.2f}\n')
    else:
        print(f'Cartão {cartao} não  efetuou nenhuma compra.\n')
    voltar_ao_menu_principal()

def relatorio_de_gastos_por_categoria():
    ler_dados_de_arquivo()
    cartao = input('Digite o número do cartão para gerar o relatório de gastos por categoria: ')
    gastos_por_categoria = {}
    for compra_item in compra:
        if compra_item['cartao'] == cartao:
            categoria = compra_item['categoria']
            valor = float(compra_item['valor'])
            if categoria in gastos_por_categoria:
                gastos_por_categoria[categoria] += valor
            else:
                gastos_por_categoria[categoria] = valor
    if gastos_por_categoria:
        print(f'Relatório de gastos por categoria para o cartão {cartao}:\n')
        for categoria, total in gastos_por_categoria.items():
            print(f'- {categoria}: R$ {total:.2f}')
        print()
    else:
        print(f'Cartão {cartao} não efetuou nenhuma compra.\n')
    voltar_ao_menu_principal()

def salvar_dados_em_arquivo():
    with open('compras.json', 'w') as arquivo:
        json.dump(compra, arquivo)

def ler_dados_de_arquivo():
    global compra
    try:
        with open('compras.json', 'r') as arquivo:
            compra = json.load(arquivo)
    except FileNotFoundError:
        compra = []

def escolher_opcao():
    try:
        opcao_escolhida = input('Digite a opção escolhida: ')
        print(f'Você escolheu a opção {opcao_escolhida}')
        if opcao_escolhida == '1':
            nova_compra()
        elif opcao_escolhida == '2':
            listar_compras()
        elif opcao_escolhida == '3':
            cancelar_compra()
        elif opcao_escolhida == '4':
            calcular_total_gasto()
        elif opcao_escolhida == '5':
            relatorio_de_gastos_por_categoria()     
        elif opcao_escolhida == '99':
            print('Saindo do programa...')
        else:
            opcao_invalida()
    except Exception as e:
        print('Ocorreu um erro ao escolher a opção:', e)

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()