// Alternar entre adicionar e atualizar pacientes
function exibir_form(tipo) {
    const add_pacientes = document.getElementById('add_pacientes');
    const att_pacientes = document.getElementById('att_pacientes');
    const relatorios = document.getElementById('relatorios');
    const historico = document.getElementById('historico');

    // Esconder todos os formulários
    if (add_pacientes) add_pacientes.style.display = "none";
    if (att_pacientes) att_pacientes.style.display = "none";
    if (relatorios) relatorios.style.display = "none";
    if (historico) historico.style.display = "none";

    // Exibir o formulário correto
    if (tipo === "1") {
        add_pacientes.style.display = "block";
    } else if (tipo === "2") {
        att_pacientes.style.display = "block";
    } else if (tipo === "3") {
        relatorios.style.display = "block";
    } else if (tipo === "4") {
        historico.style.display = "block";
    }
}


// Buscar e exibir os dados do paciente selecionado
function dados_pacientes() {
    const pacienteSelect = document.getElementById('paciente-select');
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const idPaciente = pacienteSelect.value;

    const data = new FormData();
    data.append('id_paciente', idPaciente);

    fetch('/atualizar/', {
        method: 'POST', // Certifique-se de usar POST
        headers: {
            'X-CSRFToken': csrfToken, // Inclua o CSRF Token
        },
        body: data,
    })
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            // Manipule os dados recebidos aqui
        })
        .catch((error) => console.error('Erro:', error));
}

