document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('loginForm');

    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            e.preventDefault();

            // Aquí podrías agregar una animación de carga
            const btn = this.querySelector('button');
            btn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Cargando...';

            // Simulación de envío
            setTimeout(() => {
                alert('Conectando con el sistema de autenticación...');
                btn.innerHTML = 'Ingresar al Sistema';
            }, 1000);
        });
    }
});
// ===== INTER-FICHAS =====
const botonesAccion = document.querySelectorAll('.btn-accion');
const panel = document.getElementById('panel-interfichas');
const panelContenido = document.getElementById('panel-contenido');

const contenidos = {
    torneos: `
        <h5 class="fw-bold"><i class="fas fa-list-alt me-2"></i>Lista de Torneos</h5>
        <p>Aquí se cargarán los torneos desde la base de datos.</p>`,
    inscribir: null, // Abre modal
    resultados: `
        <h5 class="fw-bold"><i class="fas fa-chart-bar me-2"></i>Resultados</h5>
        <p>Tabla de posiciones y marcadores en tiempo real.</p>`
};

if (botonesAccion.length) {
    botonesAccion.forEach(btn => {
        btn.addEventListener('click', function() {
            const seccion = this.dataset.seccion;

            if (seccion === 'inscribir') {
                new bootstrap.Modal(document.getElementById('modalInscripcion')).show();
                return;
            }

            panel.classList.remove('d-none');
            panelContenido.innerHTML = contenidos[seccion] || '';
        });
    });

    // Formulario inscripción
    const formInscripcion = document.getElementById('formInscripcion');
    if (formInscripcion) {
        formInscripcion.addEventListener('submit', function(e) {
            e.preventDefault();
            const btn = this.querySelector('button[type="submit"]');
            btn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Registrando...';
            setTimeout(() => {
                bootstrap.Modal.getInstance(document.getElementById('modalInscripcion')).hide();
                btn.innerHTML = '<i class="fas fa-check me-2"></i>Confirmar Inscripción';
                alert('¡Equipo inscrito correctamente!');
            }, 1200);
        });
    }
}
// ===== INTER-CENTROS =====
const botonesAccionCentro = document.querySelectorAll('.btn-accion-centro');
const panelCentro = document.getElementById('panel-intercentros');
const panelContenidoCentro = document.getElementById('panel-contenido-centro');

const contenidosCentro = {
    torneos: `
        <h5 class="fw-bold"><i class="fas fa-list-alt me-2"></i>Lista de Torneos Inter-Centros</h5>
        <p>Aquí se cargarán los torneos desde la base de datos.</p>`,
    resultados: `
        <h5 class="fw-bold"><i class="fas fa-chart-bar me-2"></i>Resultados Inter-Centros</h5>
        <p>Tabla de posiciones y marcadores en tiempo real.</p>`
};

if (botonesAccionCentro.length) {
    botonesAccionCentro.forEach(btn => {
        btn.addEventListener('click', function() {
            const seccion = this.dataset.seccion;
            panelCentro.classList.remove('d-none');
            panelContenidoCentro.innerHTML = contenidosCentro[seccion] || '';
        });
    });
}
// ===== GIMNASIO =====
const botonesGimnasio = document.querySelectorAll('.btn-accion-gimnasio');
const panelGimnasio = document.getElementById('panel-gimnasio');
const panelContenidoGimnasio = document.getElementById('panel-contenido-gimnasio');

const contenidosGimnasio = {
    'mis-reservas': `
        <h5 class="fw-bold"><i class="fas fa-clipboard-list me-2"></i>Mis Reservas Activas</h5>
        <p>Aquí se cargarán tus reservas activas desde la base de datos.</p>`
};

if (botonesGimnasio.length) {
    botonesGimnasio.forEach(btn => {
        btn.addEventListener('click', function() {
            const seccion = this.dataset.seccion;
            panelGimnasio.classList.remove('d-none');
            panelContenidoGimnasio.innerHTML = contenidosGimnasio[seccion] || '';
        });
    });
}
// ===== INVENTARIO =====
const botonesInventario = document.querySelectorAll('.btn-accion-inv');
const panelInventario = document.getElementById('panel-inventario');
const panelContenidoInventario = document.getElementById('panel-contenido-inventario');

const contenidosInventario = {
    devoluciones: `
        <h5 class="fw-bold"><i class="fas fa-undo me-2"></i>Devoluciones Pendientes</h5>
        <p>Aquí se cargarán las devoluciones pendientes desde la base de datos.</p>`,
    sanciones: `
        <h5 class="fw-bold"><i class="fas fa-exclamation-triangle me-2"></i>Sanciones Activas</h5>
        <p>Aquí se cargarán las sanciones activas desde la base de datos.</p>`
};

if (botonesInventario.length) {
    botonesInventario.forEach(btn => {
        btn.addEventListener('click', function() {
            const seccion = this.dataset.seccion;
            panelInventario.classList.remove('d-none');
            panelContenidoInventario.innerHTML = contenidosInventario[seccion] || '';
        });
    });
}