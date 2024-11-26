<?php

$servidor = "localhost";
$usuario = "root";
$contraseña = "Admin123";
$baseDeDatos = "php";


$conexion = new mysqli($servidor, $usuario, $contraseña, $baseDeDatos);


if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
} 

echo "Conexión exitosa";


$query = "SELECT * FROM eraikuntza";


$resultado = $conexion->query($query);


if (!$resultado) {
    die("Error en la consulta: " . $conexion->error);
}


$numregistros = $resultado->num_rows;
echo "<p>El número de eraikuntzas es: $numregistros.</p>";

$campos = $resultado->fetch_fields();


echo "<table border='2'><tr>";


foreach ($campos as $campo) {
    echo "<th>" . htmlspecialchars($campo->name) . "</th>";
}


while ($registro = $resultado->fetch_assoc()) {
    echo "<tr>";
    foreach ($registro as $campo) {
        echo "<td>" . htmlspecialchars($campo) . "</td>";
    }
    echo "</tr>";
}

echo "</table>";


$resultado->free();


$conexion->close();
echo "Conexion cerrada";
?>
