function registrar_informacao() {
    const container = document.getElementById("form-informacao");

    // HTML das opções
    const html = 
        <br>
        <div class="row">
            <div class="col-md">
                <label>Cesta de Cereais:</label>
                <select class="form-control" onchange="toggleQuantidade(this, 'quantidade-cereais') name="cereais" "> 
                    <option value="nao">Não</option>
                    <option value="sim">Sim</option>
                </select>
                <input type="number" id="quantidade-cereais" class="form-control mt-2" placeholder="Quantidade" style="display:none;">
            </div>
            <div class="col-md">
                <label>Cesta de Frutas:</label>
                <select class="form-control" onchange="toggleQuantidade(this, 'quantidade-frutas') name="frutas"">
                    <option value="nao">Não</option>
                    <option value="sim">Sim</option>
                </select>
                <input type="number" id="quantidade-frutas" class="form-control mt-2" placeholder="Quantidade" style="display:none;">
            </div>
        </div>
        <br>
        <div class="row">
            <div class="col-md">
                <label>Nutren:</label>
                <select class="form-control" onchange="toggleQuantidade(this, 'quantidade-nutren') name="nutren"">
                    <option value="nao">Não</option>
                    <option value="sim">Sim</option>
                </select>
                <input type="number" id="quantidade-nutren" class="form-control mt-2" placeholder="Quantidade" style="display:none;">
            </div>
            <div class="col-md">
                <label>Fraldas:</label>
                <select class="form-control" onchange="toggleQuantidade(this, 'quantidade-fraldas') name="fraldas"">
                    <option value="nao">Não</option>
                    <option value="sim">Sim</option>
                </select>
                <input type="number" id="quantidade-fraldas" class="form-control mt-2" placeholder="Quantidade" style="display:none;">
            </div>
        </div>
    `;

    // Inserir o HTML no container
    container.innerHTML += html;
}

// Função para exibir ou esconder o campo de quantidade
function toggleQuantidade(selectElement, inputId) {
    const input = document.getElementById(inputId);
    if (selectElement.value === "sim") {
        input.style.display = "block";
    } else {
        input.style.display = "none";
        input.value = ""; // Limpa o valor da quantidade caso "Não" seja selecionado
    }
}


function exibir_form(tipo){

    const add_paciente = document.getElementById('adicionar-paciente')
    const add_paciente = document.getElementById('att_paciente')

    if (tipo == "1"){
        att_paciente.style.display = "none"
        add_paciente.style.dispaly = "block"
    
} 
    else if (tipo == "2"){
        att_paciente.style.display = "block"
        add_paciente.style.dispaly = "none"

    }

}

function dados_pacientes(){
    paciente = document.getElementById('paciente-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value     
    console.log(csrf_token)
    id_paciente = paciente.value

    data = new FormData()
    data.append('id_paciente', id_paciente)

    fetch("/pacientes/atualiza_paciente/", {
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        }, 
        body: data
    }).then(function(result){
        return result.json()
    }).then(function(data){

        // Exibir o formulário
        document.getElementById('form-att-paciente').style.display = 'block';
    
        // Preencher os campos
        document.getElementById('nome').value = data['nome'] || '';
        document.getElementById('sobrenome').value = data['sobrenome'] || '';
        document.getElementById('cpf').value = data['cpf'] || '';
        document.getElementById('endereco').value = data['endereco'] || '';
        document.getElementById('bairro').value = data['bairro'] || '';
        document.getElementById('telefone').value = data['telefone'] || '';
        document.getElementById('data_nasc').value = data['data_nasc'] || '';
        document.getElementById('sexo').value = data['sexo'] || '';
        document.getElementById('data_entrada').value = data['data_entrada'] || '';
        document.getElementById('status').value = data['status'] || '';
    
    })
}