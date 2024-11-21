<!DOCTYPE html>
<html>
<head>
    <title>Biderketa Kalkulatu</title>
</head>
<body>
    <h1>Biderketa taula Kalkulatzeko Programa</h1>
    <form method="post" action="">
        <label for="number">Sartu zenbakia:</label>
        <input type="number" id="number" name="number" required>
        <button type="submit">Kalkulatu</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $number = intval($_POST["number"]);
        if ($number == 0 || $number == 1) {
            return 1;
        }
        else{
            for($x = 1; $x <= 10; $x++){
                $zenbakia=$number*$x;
                echo "<h2>$number x $x=$zenbakia</h2>";
        }
    }
    }
    ?>
</body>
</html>
