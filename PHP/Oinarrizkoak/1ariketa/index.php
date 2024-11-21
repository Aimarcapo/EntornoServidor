<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulario en PHP</title>
</head>

<body>
    <h1>Irudien azalera kalkulatu</h1>
    <form action="procesar.php" method="post">
        <label for="aldea">Aldea/Erradioa</label>
        <input type="text" id="aldea" name="aldea" required>
        <label for="irudia">Irudia</label>
        <select name="irudia" id="irudia">
            <option value="karratu">Karratu</option>
            <option value="triangulo">Triangulo</option>
            <option value="zirkulua">Zirkulua</option>
        </select>
        <br><br>
        <button type="submit">Kalkulatu</button>
    </form>
    <a href="../index.html">Itzuli</a>
</body>

</html>