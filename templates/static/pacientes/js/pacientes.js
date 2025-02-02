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
