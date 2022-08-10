<?php

use Alura\Banco\Modelo\Endereco;

require_once 'autoload.php';

$umEndereco = new Endereco('Petrópolis', 'bairro X', 'Rua Y', '77A');
$outroEndereco = new Endereco('Rio de Janeiro', 'bairro Y', 'Rua X', '65');

echo $umEndereco .PHP_EOL;
echo $outroEndereco .PHP_EOL;

echo $umEndereco->bairro;
exit();