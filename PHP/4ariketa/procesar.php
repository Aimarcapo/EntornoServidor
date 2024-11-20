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