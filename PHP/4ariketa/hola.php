<?php
// Iniciar la sesión
session_start();

// Inicializar las variables de sesión para contar los votos de "Sí" y "No"
if (!isset($_SESSION['votes'])) {
    $_SESSION['votes'] = [
        'Sí' => 0,
        'No' => 0
    ];
}

// Si se ha recibido un voto, actualizar la cuenta de votos
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['vote'])) {
    $vote = $_POST['vote'];
    if (array_key_exists($vote, $_SESSION['votes'])) {
        $_SESSION['votes'][$vote]++;
    }
    // Redirigir a la página de resultados después de enviar el voto
    header('Location: ' . $_SERVER['PHP_SELF']);
    exit();
}

// Preparar los datos para el gráfico
$options = array_keys($_SESSION['votes']);  // Opciones de voto (Sí y No)
$votes = array_values($_SESSION['votes']);  // Votos (los valores de la opción Sí y No)
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bozketa</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>

<?php if (!isset($_GET['resultados'])): ?>
    <!-- Formulario de votación -->
    <h1>¿Te gusta este sitio web?</h1>
    <form method="POST" action="">
        <input type="radio" name="vote" value="Sí" id="si" required>
        <label for="si">Sí</label><br>
        <input type="radio" name="vote" value="No" id="no" required>
        <label for="no">No</label><br><br>
        <button type="submit">Enviar</button>
    </form>
<?php else: ?>
    <!-- Pantalla de confirmación y resultados -->
    <h1>¡Gracias por votar!</h1>
    <p>Tu respuesta ha sido enviada correctamente.</p>
    <a href="?resultados=1"><button>Ver Resultados</button></a>
    
    <!-- Mostrar el gráfico tipo donut con los resultados -->
    <h2>Resultados de la Votación</h2>
    <canvas id="graficoDonut" width="400" height="400"></canvas>
    
    <script>
        const ctx = document.getElementById('graficoDonut').getContext('2d');
        const data = {
            labels: <?php echo json_encode($options); ?>,  // Las opciones (Sí, No)
            datasets: [{
                data: <?php echo json_encode($votes); ?>,  // Los votos
                backgroundColor: ['rgba(75, 192, 192, 0.6)', 'rgba(255, 99, 132, 0.6)'],  // Colores del gráfico
                hoverBackgroundColor: ['rgba(75, 192, 192, 1)', 'rgba(255, 99, 132, 1)'] // Colores al pasar el ratón
            }]
        };
        
        const config = {
            type: 'doughnut',  // Tipo de gráfico donut
            data: data
        };
        
        const myChart = new Chart(ctx, config);
    </script>
<?php endif; ?>

</body>
</html>
