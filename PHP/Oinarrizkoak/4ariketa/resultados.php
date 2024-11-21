<?php
session_start();
?>
<!DOCTYPE html>
<html lang="eu">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emaitzak</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <h2>Bozketaren emaitzak</h2>
    <div style="height: 250px; width: 250px;">
        <canvas id="graficoDonut" width="50" height="50"></canvas>
    </div>
    <a href="index.php"><button>Berriro bozkatu</button></a>
    <script>
        const ctx = document.getElementById('graficoDonut').getContext('2d');
        const data = {
            labels: <?php echo json_encode(array_keys($_SESSION['votes'])); ?>,
            datasets: [{
                data: <?php echo json_encode(array_values($_SESSION['votes'])); ?>,
                backgroundColor: ['rgba(75, 192, 192, 0.6)', 'rgba(255, 99, 132, 0.6)'],
                hoverBackgroundColor: ['rgba(75, 192, 192, 1)', 'rgba(255, 99, 132, 1)']
            }]
        };
        const config = {
            type: 'doughnut',
            data: data
        };
        const myChart = new Chart(ctx, config);
    </script>
</body>
</html>
