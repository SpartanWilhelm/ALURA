from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_praca.receber_avaliacao('Ana', 5)
restaurante_praca.receber_avaliacao('Bruno', 4)
restaurante_praca.receber_avaliacao('Carla', 5)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()