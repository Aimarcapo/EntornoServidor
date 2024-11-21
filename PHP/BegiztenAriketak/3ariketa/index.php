<!DOCTYPE html>
<html>
<head>
    <title>Zifrak</title>
</head>
<body>
    <h1>Zifrak kontatu</h1>
    <form method="post" action="">
        <label for="number">Sartu zenbakia:</label>
        <input type="number" id="number" name="number" required>
        <button type="submit">Kalkulatu</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $number = intval($_POST["number"]);
        function contarCifras($num) {
           $emaitza=strlen((string)$num);
            if($num<0){
                $emaitza--;
            }
            return $emaitza;
        }
        
        $zifra=contarCifras($number);
            
        echo "<h2>Zifra = $zifra</h2>";
    
    }
    ?>
</body>
</html>
