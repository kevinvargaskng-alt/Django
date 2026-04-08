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

// ===== CREAR EQUIPO =====
// Lista de jugadores
document.addEventListener('DOMContentLoaded', function () {

    // ===== LOGIN =====
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const btn = this.querySelector('button');
            btn.innerHTML = '<span class="spinner-border spinner-border-sm"></span> Cargando...';
            setTimeout(() => {
                alert('Conectando con el sistema de autenticación...');
                btn.innerHTML = 'Ingresar al Sistema';
            }, 1000);
        });
    }

    // ===== INTER-FICHAS =====
    const botonesAccion = document.querySelectorAll('.btn-accion');
    const panel = document.getElementById('panel-interfichas');
    const panelContenido = document.getElementById('panel-contenido');

    const contenidos = {
        torneos: `<h5 class="fw-bold"><i class="fas fa-list-alt me-2"></i>Lista de Torneos</h5><p>Aquí se cargarán los torneos desde la base de datos.</p>`,
        inscribir: null,
        resultados: `<h5 class="fw-bold"><i class="fas fa-chart-bar me-2"></i>Resultados</h5><p>Tabla de posiciones y marcadores en tiempo real.</p>`
    };

    if (botonesAccion.length) {
        botonesAccion.forEach(btn => {
            btn.addEventListener('click', function () {
                const seccion = this.dataset.seccion;
                if (seccion === 'inscribir') {
                    new bootstrap.Modal(document.getElementById('modalInscripcion')).show();
                    return;
                }
                panel.classList.remove('d-none');
                panelContenido.innerHTML = contenidos[seccion] || '';
            });
        });

        const formInscripcion = document.getElementById('formInscripcion');
        if (formInscripcion) {
            formInscripcion.addEventListener('submit', function (e) {
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
        torneos: `<h5 class="fw-bold"><i class="fas fa-list-alt me-2"></i>Lista de Torneos Inter-Centros</h5><p>Aquí se cargarán los torneos desde la base de datos.</p>`,
        resultados: `<h5 class="fw-bold"><i class="fas fa-chart-bar me-2"></i>Resultados Inter-Centros</h5><p>Tabla de posiciones y marcadores en tiempo real.</p>`
    };

    if (botonesAccionCentro.length) {
        botonesAccionCentro.forEach(btn => {
            btn.addEventListener('click', function () {
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
        'mis-reservas': `<h5 class="fw-bold"><i class="fas fa-clipboard-list me-2"></i>Mis Reservas Activas</h5><p>Aquí se cargarán tus reservas activas desde la base de datos.</p>`
    };

    if (botonesGimnasio.length) {
        botonesGimnasio.forEach(btn => {
            btn.addEventListener('click', function () {
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
        devoluciones: `<h5 class="fw-bold"><i class="fas fa-undo me-2"></i>Devoluciones Pendientes</h5><p>Aquí se cargarán las devoluciones pendientes desde la base de datos.</p>`,
        sanciones: `<h5 class="fw-bold"><i class="fas fa-exclamation-triangle me-2"></i>Sanciones Activas</h5><p>Aquí se cargarán las sanciones activas desde la base de datos.</p>`
    };

    if (botonesInventario.length) {
        botonesInventario.forEach(btn => {
            btn.addEventListener('click', function () {
                const seccion = this.dataset.seccion;
                panelInventario.classList.remove('d-none');
                panelContenidoInventario.innerHTML = contenidosInventario[seccion] || '';
            });
        });
    }

    // ===== CREAR EQUIPO =====
    const modalEquipo = document.getElementById('modalEquipo');
    if (modalEquipo) {
        actualizarLista();
        modalEquipo.addEventListener('hidden.bs.modal', () => {
            document.getElementById('formEquipo').reset();
            limpiarJugadores();
        });
    }

});

// ===== FUNCIONES GLOBALES DEL EQUIPO =====
// Lista de jugadores para el equipo
let jugadores = [];

function agregarJugador() {
    const input = document.getElementById('nuevoJugador');
    const nombre = input.value.trim();
    if (nombre === '') return;
    if (jugadores.includes(nombre)) {
        alert('Este jugador ya está agregado');
        return;
    }
    jugadores.push(nombre);
    actualizarLista();
    input.value = '';
    input.focus();
}

function actualizarLista() {
    const lista     = document.getElementById('listaJugadores');
    const container = document.getElementById('jugadoresContainer');
    const vacio     = document.getElementById('jugadoresVacio');
    const contador  = document.getElementById('contadorJugadores');

    if (!lista || !container || !vacio || !contador) return;

    contador.textContent = jugadores.length;

    if (jugadores.length === 0) {
        container.style.display = 'none';
        vacio.style.display     = 'block';
        lista.innerHTML = '';
        return;
    }

    container.style.display = 'block';
    vacio.style.display     = 'none';

    lista.innerHTML = jugadores.map((jugador, index) => `
        <li class="list-group-item d-flex align-items-center justify-content-between px-3 py-2"
            style="background: transparent; border-color: rgba(255,255,255,0.08); color: white;">
            <div class="d-flex align-items-center gap-2">
                <span class="badge rounded-pill"
                      style="background: rgba(255,255,255,0.1); color: rgba(255,255,255,0.6); min-width: 26px;">
                    ${index + 1}
                </span>
                <span>${jugador}</span>
            </div>
            <button type="button" class="btn btn-sm btn-danger" onclick="eliminarJugador(${index})">
                <i class="fas fa-trash"></i>
            </button>
        </li>
    `).join('');
}

function eliminarJugador(index) {
    jugadores.splice(index, 1);
    actualizarLista();
}

function limpiarJugadores() {
    jugadores = [];
    actualizarLista();
}

function guardarEquipo() {
    const nombre     = document.getElementById('nombreEquipo').value.trim();
    const tag        = document.getElementById('tagEquipo').value.trim().toUpperCase();
    const capitan    = document.getElementById('capitan').value.trim();
    const disciplina = document.getElementById('disciplina').value;

    if (!nombre || !tag || !disciplina) {
        alert("Los campos Nombre, Tag y Disciplina son obligatorios");
        return;
    }

    const formData = new FormData();
    formData.append('nombre', nombre);
    formData.append('tag', tag);
    formData.append('capitan', capitan);
    formData.append('disciplina', disciplina);
    jugadores.forEach(jugador => formData.append('jugadores[]', jugador));

    fetch('/crear-equipo/', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert(data.message);
            bootstrap.Modal.getInstance(document.getElementById('modalEquipo')).hide();
            document.getElementById('formEquipo').reset();
            limpiarJugadores();
        } else {
            alert(data.message || "Error al guardar");
        }
    })
    .catch(() => alert("Error de conexión. Inténtalo de nuevo."));
}