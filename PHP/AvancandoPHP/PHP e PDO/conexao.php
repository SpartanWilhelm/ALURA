<?php

$caminhoBanco = __DIR__ . '\banco.sqlite';
$pdo = new PDO('sqlite:' . $caminhoBanco);

Echo "Conectado ao BD!";

$pdo->exec('CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, birth_date TEXT);');

?>