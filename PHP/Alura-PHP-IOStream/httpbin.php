<?php

$contexto = stream_context_create([
    'http' => [
        'method' => 'POST',
        'header' => "X-Form: PHP\r\nContent-Type: text/plain",
        'content' => 'Teste do corpo da requisição'
    ]
]);

echo file_get_contents('http://httpbin.org/post', false, $contexto);

?>