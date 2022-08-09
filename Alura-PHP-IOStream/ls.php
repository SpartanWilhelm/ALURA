<?php

$diretoriAtual = dir('.');

echo $diretoriAtual->path . PHP_EOL;

while ($arquivo = $diretoriAtual->read()){
    echo $arquivo . PHP_EOL;
}

?>