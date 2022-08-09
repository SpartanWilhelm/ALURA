<?php

require_once 'autoload.php';

use Alura\Banco\Service\ControladorDeBonificacoes;
use Alura\Banco\Modelo\Conta\{ContaPoupanca, ContaCorrente, Titular};
use Alura\Banco\Modelo\CPF;
use Alura\Banco\Modelo\Funcionario\{Funcionario, Gerente, Diretor, Desenvolvedor,EditorVideo} ;

$umDesenvolvedor = new Desenvolvedor('Vinicius Dias', 
    new CPF ('123.456.789-00'),
    1000
);

$umDesenvolvedor->sobeDeNivel();

$umaGerente = new Gerente('Patrícia', 
    new CPF ('987.654.321-00'),
    3000
);

$umDiretor = new Diretor('Ana Maria',
    new CPF('546.987.321-89'),
    5000
);

$umEditor = new EditorVideo('Paulo', 
    new CPF('456.987.231-11'),
    1500
);

$controlador = new ControladorDeBonificacoes();
$controlador->adicionaBonificacaoDe($umDesenvolvedor);
$controlador->adicionaBonificacaoDe($umaGerente);
$controlador->adicionaBonificacaoDe($umDiretor);
$controlador->adicionaBonificacaoDe($umEditor);

echo $controlador->recuperaTotal();