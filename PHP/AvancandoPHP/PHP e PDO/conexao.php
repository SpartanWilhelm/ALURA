<?php

$caminhoBanco = __DIR__ . 'banco.sqlite';
$pdo = new PDO('sqlite:' . $caminhoBanco);


Echo "Conectado ao BD!";
?>