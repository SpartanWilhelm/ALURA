from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1 = Jogo('Yakuza', 'Hack n slash','Xbox One')
    jogo2 = Jogo('Deadfall', 'Aventura', 'PS2')
    jogo3 = Jogo('Mario Kart 7', 'Corrida', '3DS')
    jogo4 = Jogo('Mortal Kombat 1', 'Luta', 'PC')

    lista = [jogo1, jogo2, jogo3, jogo4]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run(host='0.0.0.0', port=8080)