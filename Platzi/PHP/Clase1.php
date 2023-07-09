<?php
/*Tener una lista de ciudades con un 
clima y una ubicación específica*/

function recomendacion()
{

    $clima = array(
        "Bogota" => "Frio",
        "Monteria" => "Calido", "Medellin" => "Templado"
    );

    $ubicacion = array(
        "Guajira" => "Norte",
        "Leticia" => "Sur", "Santander" => "Este", "Antioquia" => "Oeste"
    );

    $turismo = array(
        "Santa Marta" => "Mar",
        "Villavicencio" => "Llanos", "Riocha" => "Desierto", "Quindio" => "Valle"
    );

    switch ("turismo") {

        case "clima":
            echo array_search("Frio", $clima);
            break;
        case "ubicacion":
            echo array_search("Norte", $ubicacion);
            break;
        case "turismo":
            echo array_search("Mar", $turismo);
            break;
    }
}

recomendacion();
