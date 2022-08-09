<?php

namespace Alura\Banco\Conta;

use DomainException;

class SaldoInsuficienteException extends DomainException
{
    public function __construct(float $valorSaque, float $saldoAtual)
    {
        $mensagem = "Você tentou sacar $valorSaque, mas tem apenas $saldoAtual.";
        parent::__construct($mensagem);
    }
}

?>