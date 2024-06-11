from flask import Flask, render_template, request

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console

jogo1 = Jogo('Yakuza', 'Hack n slash','Xbox One')
jogo2 = Jogo('Deadfall', 'Aventura', 'PS2')
jogo3 = Jogo('Mario Kart 7', 'Corrida', '3DS')
jogo4 = Jogo('Mortal Kombat 1', 'Luta', 'PC')

lista = [jogo1, jogo2, jogo3, jogo4]

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar')
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return render_template('lista.html', titulo='Jogos', jogos=lista)

app.run(host='0.0.0.0', port=8080)