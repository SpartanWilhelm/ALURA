<?php

use Alura\Pdo\Domain\Model\Student;

require_once 'vendor/autoload.php';

$student = new Student(
    null,
    'César L. Guilherme',
    new \DateTimeImmutable('1983-05-02')
);

echo $student->age();
