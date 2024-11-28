<?php

$servidor = "localhost";
$usuario = "root";
$contraseña = "Admin123";
$baseDeDatos = "php";

$conexion = new mysqli($servidor, $usuario, $contraseña, $baseDeDatos);

if ($conexion->connect_error) {
    die("Error de conexión: " . $conexion->connect_error);
}

if ($_SERVER['REQUEST_METHOD'] == 'POST') {

    $mota = $_POST['mota'] ?? null;
    $zonaldea = $_POST['zonaldea'] ?? null;
    $helbidea = $_POST['helbidea'] ?? null;
    $logelak = $_POST['logelak'] ?? null;
    $prezioa = $_POST['prezioa'] ?? null;
    $tamaina = $_POST['tamaina'] ?? null;
    $extrak = isset($_POST['extrak']) ? implode(",", $_POST['extrak']) : null;
    $oharrak = $_POST['oharrak'] ?? null;
    $irudia = null;

    if (isset($_FILES['irudia']) && $_FILES['irudia']['error'] === UPLOAD_ERR_OK) {
        $directorioDestino = "uploads/";
        if (!is_dir($directorioDestino)) {
            mkdir($directorioDestino, 0755, true);
        }
        $nombreArchivo = basename($_FILES['irudia']['name']);
        $rutaCompleta = $directorioDestino . $nombreArchivo;

        $extensionesPermitidas = ['jpg', 'jpeg', 'png', 'gif', 'webp'];
        $extension = pathinfo($nombreArchivo, PATHINFO_EXTENSION);
        if (!in_array(strtolower($extension), $extensionesPermitidas)) {
            echo "<p>Error: Formato de imagen no permitido. Solo se permiten JPG, PNG, GIF y WEBP.</p>";
        } elseif (move_uploaded_file($_FILES['irudia']['tmp_name'], $rutaCompleta)) {
            $irudia = $nombreArchivo;
        } else {
            echo "<p>Error al mover la imagen al directorio de destino.</p>";
        }
    } elseif (isset($_FILES['irudia']) && $_FILES['irudia']['error'] !== UPLOAD_ERR_NO_FILE) {
        echo "<p>Error al subir la imagen: Código de error " . $_FILES['irudia']['error'] . "</p>";
    }

    $query = "INSERT INTO eraikuntza (mota, zonaldea, helbidea, logelak, prezioa, tamaina, extrak, irudia, oharrak)
              VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)";

    $stmt = $conexion->prepare($query);

    $stmt->bind_param("sssisdsss", $mota, $zonaldea, $helbidea, $logelak, $prezioa, $tamaina, $extrak, $irudia, $oharrak);
    echo "<p>Mota:$mota<p>";
    echo "<p>Zonaldea:$zonaldea<p>";
    echo "<p>Helbidea:$helbidea<p>";
    echo "<p>Logelak:$logelak<p>";
    echo "<p>Prezioa:$prezioa<p>";
    echo "<p>Tamaina:$tamaina<p>";
    echo "<p>Extrak:$extrak<p>";
    echo "<p>Oharrak:$oharrak<p>";

    if ($stmt->execute()) {
        echo "<p>Nuevo registro insertado exitosamente.</p>";
    } else {
        echo "<p>Error al insertar: " . $stmt->error . "</p>";
        echo "<p>Mota:$mota<p>";
        echo "<p>Zonaldea:$zonaldea<p>";
        echo "<p>Helbidea:$helbidea<p>";
        echo "<p>Logelak:$logelak<p>";
        echo "<p>Prezioa:$prezioa<p>";
        echo "<p>Tamaina:$tamaina<p>";
        echo "<p>Extrak:$extrak<p>";
        echo "<p>Oharrak:$oharrak<p>";
    }

    $stmt->close();
}

$conexion->close();
?>



<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Insertar Registro</title>
</head>

<body>
    <h1>Formulario para insertar datos en la tabla "clientes"</h1>
    <form method="POST" action="" enctype="multipart/form-data">
        <label for="mota">Tipo de propiedad:</label>
        <select name="mota" id="mota" required>
            <option value="Pisua">Pisua</option>
            <option value="Txaleta">Txaleta</option>
            <option value="Etxea">Etxea</option>
        </select><br><br>

        <label for="zonaldea">Zona:</label>
        <select name="zonaldea" id="zonaldea" required>
            <option value="Alde zaharra">Alde zaharra</option>
            <option value="Deustu">Deustu</option>
            <option value="Atxuri">Atxuri</option>
            <option value="Miribilla">Miribilla</option>
            <option value="Basurtu">Basurtu</option>
        </select><br><br>

        <label for="helbidea">Dirección:</label>
        <input type="text" name="helbidea" id="helbidea" required><br><br>

        <label for="logelak">Número de habitaciones:</label>
        <input type="radio" id="1" name="logelak" value="1">
        <label for="1">1</label>
        <input type="radio" id="2" name="logelak" value="2">
        <label for="2">2</label>
        <input type="radio" id="3" name="logelak" value="3">
        <label for="3">3</label><br><br>
        <label for="prezioa">Precio:</label>
        <input type="number" step="0.01" name="prezioa" id="prezioa" required><br><br>

        <label for="tamaina">Tamaño (m²):</label>
        <input type="number" step="0.1" name="tamaina" id="tamaina" required><br><br>

        <label for="extrak">Extras:</label>
        <input type="checkbox" id="extrak" name="extrak[]" value="Igerilekua">
        <label for="extrak">Igerilekua</label>
        <input type="checkbox" id="extrak" name="extrak[]" value="Lorategia">
        <label for="extrak">Lorategia</label>
        <input type="checkbox" id="vehicle3" name="extrak[]" value="Garajea">
        <label for="extrak">Garajea</label><br>

        <label for="irudia">Imagen:</label>
        <input type="file" name="irudia" id="irudia" accept="image/*"><br><br>

        <label for="oharrak">Observaciones:</label>
        <textarea name="oharrak" id="oharrak"></textarea><br><br>

        <button type="submit">Insertar</button>
    </form>
</body>

</html>