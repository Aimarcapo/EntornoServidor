<!DOCTYPE html>
<html>

<head>
    <title>Faktoriala Kalkulatu</title>
</head>

<body>
    <h1>Faktoriala Kalkulatzeko Programa</h1>
    <form method="post" action="">
        <label for="number">Sartu zenbakia:</label>
        <input type="number" id="number" name="number" required>
        <button type="submit">Kalkulatu</button>
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $number = intval($_POST["number"]);

        function faktoriala($zenbakia)
        {
            if ($zenbakia == 0 || $zenbakia == 1) {
                return 1;
            }
            return $zenbakia * faktoriala($zenbakia - 1);
        }

        $faktoriala = faktoriala($number);
        echo "<h2>Zenbakia: $number</h2>";
        echo "<h2>Faktoriala: $faktoriala</h2>";
    }
    ?>
</body>

</html>