<?php

namespace Alura\banco\Modelo\Funcionario;

class EditorVideo extends Funcionario
{
    public function calculaBonificacao(): float
    {
        return 600.0;
    }
}