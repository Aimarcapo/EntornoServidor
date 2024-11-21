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
        $number = $_POST["number"];

        function alderantziz($num) {
            return strrev($num); 
        }
        
        $zifra = alderantziz($number);

        if ($zifra === $number) {
            echo "<h2>Palindromoa da</h2>";
        } else {
            echo "<h2>Ez da palindromoa</h2>";
        }

        echo "<h2>Alderantziz = $zifra</h2>";
    }
    ?>
</body>
</html>
