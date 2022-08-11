<?php

namespace Alura\Pdo\Infrastructure\Repository;

use Alura\Pdo\Domain\Model\Student;
use Alura\Pdo\Domain\Repository\StudentRepository;
use Alura\Pdo\Infrastructure\Persistence\ConnectionCreator;
use DateTimeInterface;
use PDO;

class PdoStudentRepository implements StudentRepository
{
    private \PDO $connection;

    public function __construct()
    {
        $this->connection = ConnectionCreator::createConnection();
    }
    public function allStudents(): array
    {
        
    }
    public function studentsBirthAt(DateTimeInterface $birthDate): array
    {
        
    }
    public function save(Student $student): bool
    {
        if ($student->id() === null){
            return $this->insert($student);
        }   
        return $this->update($student);
    }
    public function remove(Student $student): bool
    {
        $stmt = $this->connection->prepare('DELETE FROM students WHERE id = ?;');
        $stmt->bindValue(1, $student->id(), PDO::PARAM_INT);
        
        return $stmt->execute();
    }
}

?>