document.addEventListener("DOMContentLoaded", () => {
    const switchInput = document.querySelector(".cabecalho__switch-input");
    const body = document.body;

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
        } else {
            body.classList.remove("modo-escuro");
            localStorage.setItem("modoEscuro", "disabled");
        }
    });
});

