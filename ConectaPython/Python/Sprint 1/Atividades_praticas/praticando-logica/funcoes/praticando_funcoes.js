//Exercício 1

function maior(a, b) {
    if (a > b) {
        return a;
    } if (b > a) {
        return b;
    } else {
        return "Os números são iguais";
    }
}

console.log(maior(10, 5));
console.log(maior(2, 8));
console.log(maior(4, 4));

//Exercício 2

function calculaDesconto(valorCompra, quantidadeItens){
    let valorDesconto = 0;
    if (quantidadeItens == 1) {
        valorDesconto = 0;
    } else if (quantidadeItens == 2) {
        valorDesconto = 3;
    } else if (quantidadeItens == 3) {
        valorDesconto = 7;
    } else if (quantidadeItens == 4) {
        valorDesconto = 12;
    } else {
        valorDesconto = 20;
    }
    return (valorCompra * (valorDesconto / 100)).toFixed(2);
}

console.log(calculaDesconto(150, 0)); 
console.log(calculaDesconto(137, 2)); 
console.log(calculaDesconto(256, 3)); 

//Exercício 3

function diaDaSemana(numeroDia) {
    switch (numeroDia) {
        case 1:
            return "Domingo";
        case 2:
            return "Segunda-feira";
        case 3:
            return "Terça-feira";
        case 4:
            return "Quarta-feira";
        case 5:
            return "Quinta-feira";
        case 6:
            return "Sexta-feira";
        case 7:
            return "Sábado";
        default:
            return "Número inválido";
    }
}

console.log(diaDaSemana(1));
console.log(diaDaSemana(2));
console.log(diaDaSemana(7));

//Exercício 4
function calculaFatorial(numero) {
    if (numero < 0) {
        return "Número inválido";
    } else if (numero == 0) {
        return 1;
    } else {
        let fatorial = 1;
        for (let i = 1; i <= numero; i++) {
            fatorial *= i;
        }
        return fatorial;
    }
}

console.log(calculaFatorial(5));
console.log(calculaFatorial(0));
console.log(calculaFatorial(-3));