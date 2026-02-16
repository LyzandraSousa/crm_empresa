function criarGrafico(ctx, labels, data, tipo="bar") {
    new Chart(ctx, {
        type: tipo,
        data: {
            labels: labels,
            datasets: [{
                label: 'Clientes Fechados',
                data: data,
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
