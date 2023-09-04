document.addEventListener("DOMContentLoaded", function () {
    const progressBars = document.querySelectorAll('.progress-bar');
    const hoy = new Date();

    // Calcular el progreso y aplicar el color de fondo adecuado a cada barra de progreso
    progressBars.forEach((progressBar, index) => {
        const proceso = JSON.parse(progressBar.getAttribute('data-proceso'));
        const fechaInicio = new Date(proceso.fecha_inicio);
        const fechaLimite = new Date(proceso.fecha_limite);
        const progreso = ((hoy - fechaInicio) / (fechaLimite - fechaInicio)) * 100;
        progressBar.value = progreso;

        if (progreso <= 25) {
            progressBar.style.background = '#FFFF00'; // Amarillo
        } else if (progreso <= 50) {
            progressBar.style.background = '#FFA500'; // Naranja
        } else {
            progressBar.style.background = '#FF0000'; // Rojo
        }
    });
});
