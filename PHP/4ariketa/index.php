<?php
session_start();

// Inicializar las variables de votos si no están configuradas
if (!isset($_SESSION['votes'])) {
    $_SESSION['votes'] = [
        'Sí' => 0,
        'No' => 0
    ];
}

// Redirigir a la página de resultados después de votar
if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_POST['votes'])) {
    $vote = $_POST['votes'];
    if (array_key_exists($vote, $_SESSION['votes'])) {
        $_SESSION['votes'][$vote]++;
    }
    // Redirigir al mismo archivo con un parámetro para mostrar los resultados
    header('Location: index.php?resultados=1');
    exit();
}
?>

<!DOCTYPE html>
<html lang="eu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formularioa</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h1>Formularioa</h1>
    
    <?php if (!isset($_GET['resultados'])): ?>
        <!-- Formulario de votación -->
        <form action="index.php" method="POST">
            <input type="radio" name="votes" value="Sí" id="si" required>
            <label for="si">Sí</label><br>
            <input type="radio" name="votes" value="No" id="no" required>
            <label for="no">No</label><br><br>
            <button type="submit">Enviar</button>
        </form>
    <?php else: ?>
        <!-- Pantalla de confirmación después de votar -->
        <h1>¡Gracias por votar!</h1>
        <p>Tu respuesta ha sido enviada correctamente.</p>
        <a href="?resultados=1"><button>Ver Resultados</button></a>
        
        <!-- Mostrar el gráfico tipo donut con los resultados -->
        <h2>Resultados de la Votación</h2>
        <!-- Ajuste del tamaño del gráfico (más pequeño) -->
         <div style="height: 250px; width: 250px;">
         <canvas id="graficoDonut" width="50" height="50"></canvas>
         </div>
        
        
        <script>
            const ctx = document.getElementById('graficoDonut').getContext('2d');
            const data = {
                labels: <?php echo json_encode(array_keys($_SESSION['votes'])); ?>,  // Las opciones (Sí, No)
                datasets: [{
                    data: <?php echo json_encode(array_values($_SESSION['votes'])); ?>,  // Los votos
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
