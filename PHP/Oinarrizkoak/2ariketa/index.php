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
        <label for="euro">Euro</label>
        <input type="number" id="euro" name="euro">
        <select name="txanpon" id="txanpon">
            <option value="dolar">AEBetako dolar</option>
            <option value="libera">Libera britaniar</option>
            <option value="yen">Yen japoniar</option>
            <option value="franko">Franko suitzar</option>
        </select>
        <label for="txanpon">-etan bihurtu</label>
        <br><br>
        <button type="submit">Kalkulatu</button>
    </form>
</body>

</html>
