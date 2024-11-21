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
        function alderantziz($num) {
            $signo = $num < 0 ? -1 : 1;
            $num = abs($num);
            $invertido = intval(strrev((string)$num));
            return $invertido * $signo;
        }
        
        $zifra=alderantziz($number);
            
        echo "<h2>Alderantziz = $zifra</h2>";
    
    }
    ?>
</body>
</html>
