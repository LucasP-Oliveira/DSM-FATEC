$(document).ready(function () {
    $('#cep').on('blur', function () {
        const cep = $(this).val().replace(/\D/g, "");

        if (cep.length === 8) {
            $.getJSON(`https://viacep.com.br/ws/${cep}/json/`, function (data) {
                if (!data.erro) {
                    $('#rua').val(data.logradouro);
                    $('#bairro').val(data.bairro);
                    $('#cidade').val(data.localidade);
                    $('#estado').val(data.uf);
                } else {
                    alert('CEP não encontrado!');
                    limparCampos();
                }
            }).fail(function () {
                alert('Erro ao processar o CEP.');
                limparCampos();
            });
        } else {
            alert("CEP inválido. Digite 8 números.");
            limparCampos();
        }
    });

    function limparCampos() {
        $("#rua, #bairro, #cidade, #estado").val("");
    }
});