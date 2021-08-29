
var idxSet;
var formatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'BRL',
});

$(document).ready(function() {


    $('.btnSimulate').on('click', function () {
        idxSet = $(this).data().idxproj - 1;
        console.log(idxSet);
        $('#modalSimulate').modal('show');
    })

    $('#modalSimulate').on('shown.bs.modal', function () {

        $('#cProject').html('<b>Projeto:</b> ' + list_project[idxSet].project_name);
        $('#cRisk').html('<b>Risco do Projeto:</b> ' + list_risk[list_project[idxSet].proj_risk]);
        $('#proj_amount').val(formatter.format(list_project[idxSet].proj_amount));
        $('#proj_invest').val('').trigger('focus');
        $('#result').html('');
    })

    $('#btn_simulate_now').on('click', function () {
        
        var invest = parseFloat($('#proj_invest').val()),
            amount = parseFloat(list_project[idxSet].proj_amount);
            
        if (isNaN(amount)) {
            $('#result').html('<div class="alert-warning">Sem valor de projeto para calcular o ROI!!</div>');
            return false;
        }
        
        if (isNaN(invest)) {
            $('#result').html('<div class="alert-warning">Informe um valor do investimento válido!!</div>');
            return false;
        }
        if (invest < amount) {
            $('#result').html('<div class="alert-warning">Valor de investimento deve ser maior que o valor do projeto!!</div>');
            return false;
        }

        var vperc = list_roi[list_project[idxSet].proj_risk];
        var vlroi = invest * vperc;

        $('#result').html('<div class="alert-info">Valor do ROI para o projeto: <b>' + formatter.format(vlroi) +'</b><br> (aplicado a '+ vperc* 100 +'% do investimento) </div>');

    })

})