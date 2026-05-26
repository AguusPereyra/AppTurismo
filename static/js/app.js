const info = document.getElementById("info-provincia");

const imagenProvincia = document.getElementById("imagen-provincia");

const buscador = document.getElementById("buscador");

const loader = document.getElementById("loader");

const favoritosContainer =
    document.getElementById(
        "favoritos-container"
    );

let favoritos = JSON.parse(
        localStorage.getItem("favoritos")
    ) || [];

function actualizarFavoritosMapa(){

    provincias.forEach((provincia) => {

        if(
            favoritos.includes(provincia.id)
        ){

            provincia.style.stroke = "#FFD700";

            provincia.style.strokeWidth = "2";

        }else{

            provincia.style.stroke = "white";

            provincia.style.strokeWidth = "1";
        }
    });
}

function renderFavoritos(){

    favoritosContainer.innerHTML = "";

    favoritos.forEach((favorito) => {

        favoritosContainer.innerHTML += `

            <div class="favorito-chip">

                ⭐ ${favorito}

            </div>

        `;
    });
}

const provincias = document.querySelectorAll(".mapa path");

let provinciaActual = null;
let provinciaSeleccionada = null;

function mostrarLoader(){

    info.innerHTML = `
        <div class="loader-container">
            <div class="loader"></div>
            <p>Cargando información...</p>
        </div>
    `;
}

function mostrarToast(mensaje){

    const toast =
        document.getElementById("toast");

    toast.textContent = mensaje;

    toast.classList.add("show");

    setTimeout(() => {

        toast.classList.remove("show");

    }, 2500);
}

function activarAccordion(){

    const botonesAccordion = document.querySelectorAll(".accordion-btn");

    botonesAccordion.forEach((boton) => {
        boton.addEventListener("click", () => {
            const contenido = boton.nextElementSibling;
            contenido.classList.toggle("active");
        });
    });

}

function renderProvincia(provincia, datos){
    const esFavorita = favoritos.includes(
        provincia.id
    );
    let contenido = `

                <button
                    class="favorito-btn"
                    onclick="toggleFavorito(&quot;${provincia.id}&quot;)"
                >

                    ${esFavorita ? "⭐" : "☆"}

                </button>
                <h2>PROVINCIA TEST</h2>
                <div class="accordion">
                    <button class="accordion-btn">
                        🎵 Eventos
                    </button>
                    <div class="accordion-content">
                        <ul>
                            ${datos.eventos?.length > 0

                                ? datos.eventos.map(evento => `

                                    <div class="evento-card">

                                        <img
                                            src="/static/img/eventos/${evento.imagen}"
                                            class="evento-img"
                                        >

                                        <h3>${evento.nombre}</h3>

                                        <p>📅 ${evento.fecha}</p>

                                        <p>📍 ${evento.lugar}</p>

                                    </div>

                                `).join("")

                                : "<p>No hay eventos disponibles</p>"
                                }
                        </ul>
                    </div>

                    <button class="accordion-btn">
                        🍴 Gastronomía
                    </button>

                    <div class="accordion-content">

                        ${datos.gastronomia?.length > 0 ? `

                            <ul>

                                ${datos.gastronomia.map(comida => `

                                    <li>${comida}</li>

                                `).join("")}

                            </ul>

                        `

                        : "<p>No hay gastronomía disponible</p>"
                        }

                    </div>

                    <button class="accordion-btn">
                        📍 Turismo
                    </button>

                    <div class="accordion-content">

                        ${datos.turismo?.length > 0 ? `

                            <ul>

                                ${datos.turismo.map(lugar => `

                                    <li>${lugar}</li>

                                `).join("")}

                            </ul>

                        `

                        : "<p>No hay lugares turísticos disponibles</p>"
                        }

                    </div>
                </div>
            `;
            info.innerHTML = contenido;

            info.style.animation = "none";

            void info.offsetWidth;

            info.style.animation =
                "fadeSlide 0.35s ease";
            
            activarAccordion();
}


provincias.forEach((provincia) => {
    provincia.addEventListener("click", async () => {
        provincias.forEach((p) => {

            p.style.fill = "#334155";

            if(favoritos.includes(p.id)){

                p.style.stroke = "#FFD700";

            }else{

                p.style.stroke = "white";
            }

            p.style.strokeWidth = "1";
        });

        provincia.style.fill = "#2563eb";

        provincia.style.stroke = "#60a5fa";

        provincia.style.strokeWidth = "3";

        provinciaSeleccionada = provincia.id;

        mostrarLoader();

        try{
                loader.classList.remove("hidden");

                const respuesta = await fetch(`/api/provincia/${provincia.id}`);

                const datos = await respuesta.json();

                info.classList.remove("fade-in");
                renderProvincia(provincia, datos);

                setTimeout(() => {
                    info.classList.add("fade-in");
                }, 10);

                info.scrollIntoView({
                    behavior: "smooth"
                });

                loader.classList.add("hidden");
            }

        catch(error){

            info.innerHTML = `
                <div class="error-box">

                    <h2>⚠ Error</h2>

                    <p>
                        No se pudo cargar la provincia
                    </p>

                </div>
            `;

            loader.classList.add("hidden");

            console.error(error);
        }

    });
});

buscador.addEventListener("input", () => {

    const valor = buscador.value.toLowerCase();

    provincias.forEach((provincia) => {

        if(valor === ""){

            provincia.style.fill = "#334155";

        }

        else if(
            provincia.id
            .toLowerCase()
            .includes(valor)
        ){

            provincia.style.fill = "#3b82f6";

        }else{

            provincia.style.fill = "#334155";
        }
    });
});

buscador.addEventListener("keydown", (e) => {

    if(e.key === "Enter"){

        const valor = buscador.value.toLowerCase();

        const provinciaEncontrada = Array.from(
            provincias
        ).find((provincia) => {

            return provincia.id
                .toLowerCase()
                .includes(valor);
        });

        if(provinciaEncontrada){

            provinciaEncontrada.dispatchEvent(
                new Event("click")
            );
        }
    }
});

function toggleFavorito(nombreProvincia){

    if(favoritos.includes(nombreProvincia)){

        favoritos = favoritos.filter(
            fav => fav !== nombreProvincia
        );
        mostrarToast(
            `❌ ${nombreProvincia} eliminado`
        );

    }else{

        favoritos.push(nombreProvincia);
        mostrarToast(
            `⭐ ${nombreProvincia} agregado a favoritos`
        );
    }

    localStorage.setItem(
        "favoritos",
        JSON.stringify(favoritos)
    );

    actualizarFavoritosMapa();

    renderFavoritos();

    const provinciaActiva = Array.from(
        provincias
    ).find(
        provincia => provincia.id === nombreProvincia
    );

    if(provinciaActiva){

        provinciaActiva.dispatchEvent(
            new Event("click")
        );
    }
}

function init(){

    actualizarFavoritosMapa();

    renderFavoritos();
}

init();

window.toggleFavorito = toggleFavorito;

