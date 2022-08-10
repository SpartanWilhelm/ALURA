<?php

namespace Alura\Banco\Modelo\Funcionario;

use Alura\Banco\Modelo\Pessoa;
use Alura\banco\Modelo\CPF;
use Alura\Banco\Modelo\Funcionario\{Funcionario, Gerente, Diretor};

abstract class Funcionario extends Pessoa
{
    private $salario;

    public function __construct(string $nome, CPF $cpf, float $salario)
    {
        parent::__construct($nome, $cpf);
        $this->salario = $salario;
    }

    public function recuperaCargo(): string
    {
        return $this->cargo;
    }

    public function recebeAumento(float $valorAumento): void 
    {
        if ($valorAumento <0) {
            echo "Aumento deve ser positivo!";
            return;
        }
        $this->salario += $valorAumento;
    }

    public function recuperaSalario(): float
    {
        return $this->salario;
    }

    public function alteraNome(string $nome): void
    {
        $this->validaNome($nome);
        $this->nome = $nome;
    }

    abstract public function calculaBonificacao(): float;
}
