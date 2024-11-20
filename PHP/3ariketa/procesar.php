<?php

// POST metodoa erabiltzen dela ziurtatu
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Aldea balidatu
    $izena = htmlspecialchars($_POST['izena']);
    $testua = htmlspecialchars($_POST['testua']);
    $mota = htmlspecialchars($_POST['mota']);
    
       
  

    // Irudiaren informazioa
    $irudiIzena = $_FILES['irudia']['name'];
    $irudiTemp = $_FILES['irudia']['tmp_name'];
    $irudiErrorea = $_FILES['irudia']['error'];

    // Irudia balidatu eta igo
    $irudiaIgoa = "";
    if (!empty($irudiIzena)) {
        // Onartutako formatuak
        $onartutakoFormatuak = ['jpg', 'jpeg', 'png', 'gif'];
        $irudiExt = strtolower(pathinfo($irudiIzena, PATHINFO_EXTENSION));

        // Balidatu irudia
        if (!in_array($irudiExt, $onartutakoFormatuak)) {
            die("<h1>Errorea: Igo irudi bat (JPG, PNG edo GIF formatukoa).</h1>");
        }

        // Fitxategia igo
        $helburua = "irudiak/" . basename($irudiIzena);
        if (move_uploaded_file($irudiTemp, $helburua)) {
            $irudiaIgoa = $helburua; // Gorde fitxategiaren helburua
        } else {
            die("<h1>Errorea: Irudia igotzerakoan akatsa gertatu da.</h1>");
        }
    }

    // Emaitzak erakutsi
    echo "<h1>Formularioa prozesatua</h1>";
    echo "<p><strong>Izena:</strong> $izena</p>";
    echo "<p><strong>Testua:</strong> $testua</p>";
    echo "<p><strong>Mota:</strong> $mota</p>";
    if (!empty($irudiaIgoa)) {
        echo "<p><strong>Irudia:</strong> <a href='$irudiaIgoa' download>$irudiIzena</a></p>";
    } else {
        echo "<p><strong>Irudia:</strong> Ez da irudirik igo.</p>";
    }
} else {
    echo "<h1>Errorea: Sarbidea ez da zuzena.</h1>";
}
?>
