<?php

function deletee($ids, $conexion)
{
   
    $placeholders = implode(',', array_fill(0, count($ids), '?'));
    $stmt = $conexion->prepare("DELETE FROM eraikuntza WHERE id IN ($placeholders)");

   
    $stmt->bind_param(str_repeat('i', count($ids)), ...$ids);
    $stmt->execute();
    $stmt->close();
}

$servidor = "localhost";
$usuario = "root";
$contraseña = "Admin123";
$baseDeDatos = "php";

$conexion = new mysqli($servidor, $usuario, $contraseña, $baseDeDatos);

if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}

echo "Conexión exitosa<br>";

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['id_eliminar'])) {
    $ids_eliminar = array_map('intval', $_POST['id_eliminar']); 
    deletee($ids_eliminar, $conexion);
    echo "<p>Registros eliminados correctamente.</p>";
}

$query = "SELECT * FROM eraikuntza";
$resultado = $conexion->query($query);

if (!$resultado) {
    die("Error en la consulta: " . $conexion->error);
}

$numregistros = $resultado->num_rows;
echo "<p>El número de eraikuntzas es: $numregistros.</p>";

$campos = $resultado->fetch_fields();

echo "<form method='POST' onsubmit=\"return confirm('¿Seguro que deseas eliminar los registros seleccionados?');\">";
echo "<table border='2'><tr>";
foreach ($campos as $campo) {
    echo "<th>" . htmlspecialchars($campo->name) . "</th>";
}
echo "<th>Seleccionar</th>";
echo "</tr>";

while ($registro = $resultado->fetch_assoc()) {
    echo "<tr>";
    foreach ($registro as $nombreCampo => $valorCampo) {
        if ($nombreCampo === 'irudia' && !empty($valorCampo)) {
            echo "<td><a href='uploads/" . htmlspecialchars($valorCampo) . "' target='_blank'>Ikusi irudia</a></td>";
        } elseif ($nombreCampo === 'irudia' && empty($valorCampo)) {
            echo "<td>Sin imagen</td>";
        } else {
            echo "<td>" . htmlspecialchars($valorCampo) . "</td>";
        }
    }
    echo "<td>
            <input type='checkbox' name='id_eliminar[]' value='" . htmlspecialchars($registro['id']) . "'>
        </td>";
    echo "</tr>";
}

echo "</table>";
echo "<button type='submit'>Eliminar seleccionados</button>";
echo "</form>";

$resultado->free();
$conexion->close();
echo "Conexión cerrada";
?>
