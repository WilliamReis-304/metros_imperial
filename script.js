// Função de callback para calcular a gorjeta com base na qualidade do serviço
const calcularGorjeta = () => {
    const totalConta = parseFloat(document.getElementById("totalConta").value);
    const qualidadeServico = document.getElementById("qualidadeServico").value;

    // Validação para garantir que o valor da conta é um número positivo
    if (isNaN(totalConta) || totalConta <= 0) {
        document.getElementById("resultadoGorjeta").innerText = "Por favor, insira um valor válido para a conta.";
        return;
    }

// Definir as porcentagens de gorjeta com base na qualidade do serviço
const calcularPorcentagem = (qualidade, callback) => {
        let porcentagem;
        if (qualidade === "bom") {
            porcentagem = 0.20;
        } else if (qualidade === "regular") {
            porcentagem = 0.10;
        } else if (qualidade === "ruim") {
            porcentagem = 0.05;
        }
        return callback(porcentagem);
    };

// Arrow function para calcular o valor da gorjeta
const calcularValorGorjeta = porcentagem => totalConta * porcentagem;

// Chamada da função de callback para obter o resultado final
const valorGorjeta = calcularPorcentagem(qualidadeServico, calcularValorGorjeta);

// Exibir o resultado
document.getElementById("resultadoGorjeta").innerText = `Gorjeta: R$ ${valorGorjeta.toFixed(2)}`;
};
