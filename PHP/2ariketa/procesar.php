<?php

if ($_SERVER["REQUEST_METHOD"] === "POST") {


    $euro = htmlspecialchars($_POST['euro']);
    $txanpon = htmlspecialchars($_POST['txanpon']);

    if (!empty($euro) && is_numeric($euro) && $euro > 0) {

        if ($txanpon === "dolar") {
            $total = $euro*1.08;
            echo "<p>$euro euro $total dolar dira</p>";
        } elseif ($txanpon === "libera") {
            $total = $euro*0.83;
            echo "<p>$euro euro $total libera britaniar dira</p>";
        } elseif ($txanpon === "yen") {
            $total = $euro*164.3;
            echo "<p>$euro euro $total yen japoniar dira</p>";
        }
        elseif ($txanpon === "franko") {
            $total = $euro*0.94;
            echo "<p>$euro euro $total franko suitzar dira</p>";
        }
        

    } else {

        echo "<h1>Error en el formulario</h1>";
        echo "<p>Por favor, ingresa un número válido para el valor.</p>";
    }
} else {
    echo "<h1>Acceso no permitido</h1>";
    echo "<p>Este archivo solo procesa datos enviados desde un formulario.</p>";
    
}
