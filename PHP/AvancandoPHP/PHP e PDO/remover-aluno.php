<?php

require_once 'vendor/autoload.php';

$databasePath = __DIR__ . '\banco.sqlite';
$pdo = new PDO('sqlite:' . $databasePath);

$preparedStatement = $pdo->prepare('DELETE FROM students Where id = ?;');
$preparedStatement->bindValue(1,2,PDO::PARAM_INT);
var_dump($preparedStatement->execute());

?>