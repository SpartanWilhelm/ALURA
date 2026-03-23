let listaPalavrasPossiveis = ['banana', 'abacaxi', 'laranja', 'uva', 'manga'];
let palavraSecreta = listaPalavrasPossiveis[Math.floor(Math.random() * listaPalavrasPossiveis.length)];
let letrasCorretas = [];
let tentativas = 5;

while (tentativas > 0) {
    const prompt = require('prompt-sync')();
let letra = prompt('Digite uma letra: ').toLowerCase();
console.log(`Você digitou: ${letra}`);


    if (letra.length != 1) {
        console.log('Por favor, digite apenas uma letra.');
        continue;
    }

    if (letrasCorretas.includes(letra)) {
        console.log('Você já tentou essa letra.');
        continue;
    }

    letrasCorretas.push(letra);

    if (palavraSecreta.includes(letra)) {
        console.log('Boa! A letra está na palavra.');
    } else {
        console.log('Ops! A letra não está na palavra.');
        tentativas--;
    }

    let palavraAtual = '';
    for (let i = 0; i < palavraSecreta.length; i++) {
        if (letrasCorretas.includes(palavraSecreta[i])) {
            palavraAtual += palavraSecreta[i];
        } else {
            palavraAtual += '_';
        }
    }

    console.log('Palavra atual: ' + palavraAtual);
    console.log('Tentativas restantes: ' + tentativas);

    if (palavraAtual == palavraSecreta) {
        console.log('Parabéns! Você adivinhou a palavra: ' + palavraSecreta);
        break;
    }

    if (tentativas == 0) {
        console.log('Fim de jogo! A palavra era: ' + palavraSecreta);
    }
}   