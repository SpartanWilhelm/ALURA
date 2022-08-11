<?php

$pdo = \Alura\Pdo\Infrastructure\Persistence\ConnectionCreator::createConnection();

Echo "Conectado ao BD!";

$pdo->exec('CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, birth_date TEXT);');

?>