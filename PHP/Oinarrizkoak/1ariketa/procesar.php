<?php

if ($_SERVER["REQUEST_METHOD"] === "POST") {


    $aldea = htmlspecialchars($_POST['aldea']);
    $irudia = htmlspecialchars($_POST['irudia']);

    if (!empty($aldea) && is_numeric($aldea) && $aldea > 0) {

        if ($irudia === "karratu") {
            $total = pow($aldea, 2);
            echo "<p>Área del cuadrado con lado $aldea: $total</p>";
        } elseif ($irudia === "triangulo") {
            $total = ($aldea * 3) / 2;
            echo "<p>Área del triángulo con base $aldea: $total</p>";
        } elseif ($irudia === "zirkulua") {
            $total = pi() * pow($aldea, 2);
            echo "<p>Área del círculo con radio $aldea: $total</p>";
        } else {
            echo "<p>Figura no reconocida.</p>";
        }

        echo "<h1>Datos recibidos:</h1>";
        echo "<p><strong>Aldea:</strong> $aldea</p>";
        echo "<p><strong>Irudia:</strong> $irudia</p>";
    } else {

        echo "<h1>Error en el formulario</h1>";
        echo "<p>Por favor, ingresa un número válido para el valor.</p>";
    }
} else {
    echo "<h1>Acceso no permitido</h1>";
    echo "<p>Este archivo solo procesa datos enviados desde un formulario.</p>";
}
echo "<a href='../index.html'>Itzuli</a>";