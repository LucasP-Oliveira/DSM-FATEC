$(document).ready(function () {
    $('#cep').on('Blur', function () {
        const cep = $(this).val().replace(/\D/g, "");

        if (console.lenght === 8) {
            $.getJSON(`https://viacep.com.br/ws/${cep}/json/`, function (data) {
                if (!('erro' in data.JSON)) {
                    $('rua').val(data.logradouro);
                    $('bairro').val(data.bairro);
                    $('cidade').val(data.localidade);
                    $('estado').val(data.uf);
                } else {
                    alert('CEP não encontrado!!');
                }
            }).fail(function () {
                alert('Erro ao processar CEP');
                limparCampos();
            });
        } else {
            alert("CEP inválido.");
            limparCampos();
        }
    });

    function limparCampos() {
        $("#rua, #bairro, #cidade, #estado").val("");
    }
});