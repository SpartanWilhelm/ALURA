<?php

require_once 'vendor/autoload.php';

$pdo = \Alura\Pdo\Infrastructure\Persistence\ConnectionCreator::createConnection();

$preparedStatement = $pdo->prepare('DELETE FROM students Where id = ?;');
$preparedStatement->bindValue(1,3,PDO::PARAM_INT);
if($preparedStatement->execute()){
    echo "Aluno excluído!";
}else{
    echo "Erro ao excluir o aluno!";
}

?>