$("#calcular").click(function () {
    var v1 = parseFloat($('#txtvalor1').val());
    var v2 = parseFloat($('#txtvalor2').val());
    var v3 = parseFloat($('#txtvalor3').val());

    if (isNaN(v1) || isNaN(v2) || isNaN(v3)) {
        alert('Por favor, insira números válidos')
        return;
    }

    var media = parseFloat(((v1 + v2 + v3) / 3).toFixed(2));

    var moeda = media.toLocaleString('pt-BR',
        {
            style: 'currency',
            currency: 'BRL',
            minimumFractionDigits: 2,
        });

    $('#txtmedia')
        .text('A média é: ' + moeda)
        .css({
            'font-weight': 'bold',
            'font-size': '18pt',
            'color': '#00f'
        })
        .fadeIn(1000);

    if (media > 6) {
        alert('Valor acima de 6: ' + media);
        console.log('Valor acima de 6; ' + media);
        $('#txtmsg')
            .text('Valor acima de 6: ' + media)
            .css({
                'font-weight': 'bold',
                'font-size': '18pt',
                'color': '#f0f',
            });
    } else {
        alert('Valor menor ou igual a 6: ' + media);
        console.log('Valor menor ou igual a 6; ' + media);
        $('#txtmsg')
            .text('Valor menor ou igual a 6: ' + media)
            .css({
                'font-weight': 'bold',
                'font-size': '18pt',
                'color': '#0f0',
            });
    }

    //if ternário - decisão em uma linha

    var mostrar = 'da média';
    mostrar = (media > 6) ? 'Acima ' + mostrar : 'Abaixo ' + mostrar;
    alert('If Ternário - Resultado: ' + mostrar)

    //estrutura de decisão - switch case

    var msg = 'A média é ';
    switch (parseInt(media)) {
        case 0:
            msg += 'par';
            break;

        case 1:
            msg += 'impar';
            break;

        default:
            msg = 'Erro';
            break;
    }

    alert(msg);

    switch (true) {
        case (media > 10):
            msg = 'Maior que 10';
            break;

        case (media > 5):
            msg = 'Maior que 5';

        default:
            msg = 'Menor ou igual a 5';
            break;
    }

    alert(msg)

    // Fatorial

    var fatorial = 1;
    for (var i = 1; i <= v1; i++) {
        fatorial *= i;
    }

    $('#txtfatorial')
        .text('O formato é: ' + fatorial)
        .css({ 'font-weight': 'bold', 'font-size': '18pt', 'color': '#0f0' })

});


