alert('Boas vindas ao jogo do número secreto!');
let tamanhoMaximo = prompt('Defina o tamanho máximo do número:');
let numeroSecreto = parseInt(Math.random() * tamanhoMaximo) + 1;
let chute;
let tentativas = 1;

//enquanto
while (chute != numeroSecreto) {
    chute = prompt(`Escolha um número entre 1 e ${tamanhoMaximo}:`);
    //Se chute for igual ao número secreto, exiba uma mensagem de sucesso
    if (chute == numeroSecreto) {
        break;
    } else {        
        if(chute < numeroSecreto) {
            alert(`O número secreto é maior que o seu chute. ${chute}`);
        } else {
            alert(`O número secreto é menor que o seu chute. ${chute}`);
        }
        tentativas++;
    }
}

let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa';
alert(`Isso aí! Você descobriu o número secreto! ${numeroSecreto} com ${tentativas} ${palavraTentativa}.`);



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