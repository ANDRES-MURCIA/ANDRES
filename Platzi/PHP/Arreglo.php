<?php
function process($busqueda, $tipo)
{
    $clima = array(
        'Bogota' => 'frio',
        'Monteria' => 'calido',
        'Medellin' => 'templado'
    );

    $ubicacion = array(
        'Guajira' => 'Norte',
        'Leticia' => 'Sur',
        'Santander' => 'Este',
        'Antioquia' => 'Oeste'
    );

    $turismo = array(
        'Santa Marta' => 'Mar',
        'Villavicencio' => 'Llano',
        'Riohacha' => 'Desierto',
        'Quindio' => 'Valle'
    );

    switch ($busqueda) {
        case 'clima':
            echo array_search($tipo, $clima);
            break;
        case 'ubicacion':
            echo array_search($tipo, $ubicacion);
            break;
        case 'turismo':
            echo array_search($tipo, $clima);
            break;
    }
}

process("clima", "frio");
