//Exercício 1

let lista = [2, 5, 3];
let soma = 0;

for (let i = 0; i < lista.length; i++) {
    soma += lista[i];
}
console.log(soma);

//Exercício 2

let listaMax = [10, 7, 22, 15];
let max = 0;
for (let i = 0; i < listaMax.length; i++) {
    if (listaMax[i] > max) {
        max = listaMax[i];
    }
}
console.log(max);

//Exercício 3
let listaNumeros = [1, 2, 3, 4, 5, 6];
let numerosPares = [];

for (let i = 0; i < listaNumeros.length; i++) {
    if (listaNumeros[i] % 2 == 0) {
        numerosPares.push(listaNumeros[i]);
    }
}
console.log(numerosPares);

//Exercício 4
let listaFaturamentoPorMes = [['janeiro', 10], ['fevereiro', 20], ['março', 30]];
let faturamento = 0;

for (let i=0; i< listaFaturamentoPorMes.length; i++) {
    faturamento += listaFaturamentoPorMes[i][1];
}
console.log(faturamento);