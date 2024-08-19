// Função para converter metros para outras unidades de comprimento
const converterUnidade = () => {
    const metros = parseFloat(document.getElementById("metros").value);
    const unidadeDestino = document.getElementById("unidadeDestino").value;
    let resultado;

    // Validação para garantir que o valor inserido é positivo
    if (isNaN(metros) || metros <= 0) {
        document.getElementById("resultado").innerText = "Por favor, insira um valor válido em metros.";
        return;
    }

// Realizar a conversão com base na unidade de destino selecionada
switch (unidadeDestino) {
    case "jarda":
        resultado = metros * 1.094;
        document.getElementById("resultado").innerText = `${metros} metros é igual a ${resultado.toFixed(3)} jardas.`;
        break;
    case "pe":
        resultado = metros * 3.281;
        document.getElementById("resultado").innerText = `${metros} metros é igual a ${resultado.toFixed(3)} pés.`;
        break;
    case "polegada":
        resultado = metros * 39.37;
        document.getElementById("resultado").innerText = `${metros} metros é igual a ${resultado.toFixed(3)} polegadas.`;
        break;
    case "milha":
        resultado = metros * 0.000621;
        document.getElementById("resultado").innerText = `${metros} metros é igual a ${resultado.toFixed(6)} milhas.`;
        break;
    default:
        document.getElementById("resultado").innerText = "Selecione uma unidade de medida válida.";
}
};
