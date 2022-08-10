<?php

use Alura\Banco\Modelo\Conta\{ContaPoupanca, ContaCorrente, Titular};
use Alura\Banco\Modelo\{CPF, Endereco};

require_once 'autoload.php';

$conta = new ContaPoupanca(
    new Titular(
        new CPF(numero: '123.456.789-00'), 
        'Vinícius Dias', 
        new Endereco(cidade: 'Petropolis', bairro: 'bairro teste', rua: 'Rua Lá', numero: '37')
    )
);
$conta->deposita(valorADepositar: 500);
$conta->saca(valorASacar: 100);

echo $conta->recuperaSaldo();