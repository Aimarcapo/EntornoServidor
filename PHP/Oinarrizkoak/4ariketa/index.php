<?php
session_start();

if (!isset($_SESSION['votes'])) {
    $_SESSION['votes'] = [
        'Bai' => 0,
        'Ez' => 0
    ];
}

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['votes'])) {
    $vote = $_POST['votes'];
    if (array_key_exists($vote, $_SESSION['votes'])) {
        $_SESSION['votes'][$vote]++;
    }
    header('Location: resultados.php');
    exit();
}
?>
<!DOCTYPE html>
<html lang="eu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formularioa</title>
</head>
<body>
    <h1>Formularioa</h1>
    <form action="index.php" method="POST">
        <input type="radio" name="votes" value="Bai" id="si" required>
        <label for="si">Bai</label><br>
        <input type="radio" name="votes" value="Ez" id="no" required>
        <label for="no">Ez</label><br><br>
        <button type="submit">Bidali</button>
    </form>
</body>
</html>
