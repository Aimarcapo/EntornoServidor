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
        <label for="number2">Sartu zenbakia handiagoa:</label>
        <input type="number" id="number2" name="number2" required>
        <button type="submit">Kalkulatu</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $number = intval($_POST["number"]);
        $number2 = intval($_POST["number2"]);
        
        function rangoa($inicio, $fin) {
            return range(min($inicio, $fin), max($inicio, $fin));
        }

        function esPrimo($num) {
            if ($num <= 1) return false;
            for ($i = 2; $i <= sqrt($num); $i++) {
                if ($num % $i == 0) return false;
            }
            return true;
        }

        $numeros = rangoa($number, $number2);
        $primos = array_filter($numeros, "esPrimo");

        echo "<h2>Zenbakiak lehenak: " . implode(", ", $primos) . "</h2>";
    }
    ?>
</body>
</html>
