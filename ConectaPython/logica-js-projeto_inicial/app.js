alert('Boas vindas ao jogo do número secreto!');
let numeroSecreto = 5;
let chute = prompt('Escolha um número entre 1 e 30:');

//Se chute for igual ao número secreto, exiba uma mensagem de sucesso
if (chute == numeroSecreto) {
    alert(`Isso aí! Você descobriu o número secreto! ${numeroSecreto}`);
} else {
    alert('Que pena! Você errou o número secreto.');
}



/*
Desafio aula 1
alert("Boas vindas ao nosso site!");
let nome = "Lua";
let idade = 25;
let numeroDeVendas = 50;
let saldoDisponivel = 1000;
let mensagemDeErro = "Erro! Preencha todos os campos";
let nome = prompt("Qual o seu nome?");
let idade = prompt("Qual a sua idade?");
if (idade >= 18) {
    alert("Você pode tirar a habilitação!");
};
*/