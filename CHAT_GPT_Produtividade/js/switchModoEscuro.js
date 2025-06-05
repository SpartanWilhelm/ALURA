document.addEventListener("DOMContentLoaded", () => {
    const switchInput = document.querySelector(".cabecalho__switch-input");
    const body = document.body;
    const logo = document.getElementById('logo-vidflow');

    // Verificar estado armazenado no localStorage
    const modoEscuroAtivado = localStorage.getItem("modoEscuro") === "enabled";

    if (modoEscuroAtivado) {
        body.classList.add("modo-escuro");
        switchInput.checked = true;
    }

    switchInput.addEventListener("change", () => {
        if (switchInput.checked) {
            body.classList.add("modo-escuro");
            localStorage.setItem("modoEscuro", "enabled"); // Salva a preferência do usuário
            logo.src = './img/modo_escuro/vidflow-logo-dark-mode.png';
        } else {
            body.classList.remove("modo-escuro");
            localStorage.setItem("modoEscuro", "disabled");
            logo.src = './img/modo_claro/vidflow-logo-light-mode.png';
        }
    });
});

