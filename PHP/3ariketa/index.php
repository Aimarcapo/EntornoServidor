<!DOCTYPE html>
<html lang="eu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formularioa</title>
    <script>
        function validateForm() {
           
            const aldea = document.getElementById("aldea").value.trim();
            const irudia = document.getElementById("irudia").value;

           
            if (!aldea || isNaN(aldea) || aldea <= 0) {
                alert("Mesedez, idatzi aldea (zenbaki bat eta positiboa izan behar du).");
                return false;
            }

            
            if (irudia) {
                const allowedExtensions = /(\.jpg|\.jpeg|\.png|\.gif)$/i;
                if (!allowedExtensions.test(irudia)) {
                    alert("Mesedez, igo irudi bat (JPG, PNG edo GIF formatukoa).");
                    return false;
                }
            }

            return true;
        }
    </script>
</head>
<body>
    <h1>Formularioa</h1>
    <form action="procesar.php" method="post" enctype="multipart/form-data" onsubmit="return validateForm()">
        <label for="izena">Izenburua*:</label>
        <input type="text" id="izena" name="izena" required>
        <br><br>
        <label for="testua">Testua*:</label>
        <textarea id="testua" name="testua" rows="4" cols="50" required></textarea>
        <br>
        <select name="mota" id="mota">
            <option value="eskaintzak">Eskaintzak</option>
            <option value="libera">Libera britaniar</option>
            <option value="yen">Yen japoniar</option>
            <option value="franko">Franko suitzar</option>
        </select>
        <br>
        <label for="irudia">Irudia (ez derrigorrezkoa):</label>
        <input type="file" id="irudia" name="irudia" accept=".jpg, .jpeg, .png, .gif">
        <br><br>

        <button type="submit">Bidali</button>
    </form>
</body>
</html>
