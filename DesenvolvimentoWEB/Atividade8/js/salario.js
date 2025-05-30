$(document).ready(function() {
    // Função para calcular o salário quando o botão for clicado
    $("#calcularSalario").click(function() {
        // Obter os valores dos campos
        const nome = $("#txtNome").val();
        const idade = parseInt($("#txtIdade").val());
        const salarioBruto = parseFloat($("#txtSalarioBruto").val());
        const dependentes = parseInt($("#selDependentes").val());
        
        // Validar se todos os campos foram preenchidos
        if (!nome || isNaN(idade) || isNaN(salarioBruto)) {
            alert("Por favor, preencha todos os campos corretamente.");
            return;
        }
        
        // Calcular bônus por idade
        const bonusIdade = idade > 50 ? 300 : 200;
        
        // Calcular INSS (8% do salário bruto)
        const inss = salarioBruto * 0.08;
        
        // Calcular Vale Transporte (5% do salário bruto)
        const valeTransporte = salarioBruto * 0.05;
        
        // Calcular valor por dependentes (50 reais por dependente)
        const valorDependentes = dependentes * 50;
        
        // Calcular salário líquido
        const salarioLiquido = salarioBruto - inss - valeTransporte + bonusIdade + valorDependentes;
        
        // Exibir resultado em alerta
        const mensagem = 
            "Nome: " + nome + "\n" +
            "Número de Dependentes: " + dependentes + "\n" +
            "Salário Bruto: R$ " + salarioBruto.toFixed(2) + "\n" +
            "INSS: R$ " + inss.toFixed(2) + "\n" +
            "Vale Transporte: R$ " + valeTransporte.toFixed(2) + "\n" +
            "Bônus por Idade: R$ " + bonusIdade.toFixed(2) + "\n" +
            "Valor por Dependentes: R$ " + valorDependentes.toFixed(2) + "\n" +
            "Salário Líquido: R$ " + salarioLiquido.toFixed(2);
        
        alert(mensagem);
    });
});
