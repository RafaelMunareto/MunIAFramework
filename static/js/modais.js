$(document).ready(function(){
    
    $(".bancario").click(function(){
        var url = $(this).attr("data-id");
        $(".loading").addClass('display-block');
        $("#bancarios").modal('open');
        $('#bancario_result').html('').load(url, function(){
            $(".loading").removeClass('display-block').addClass('display-none')
        });
    });

    $(".contato").click(function(){
        var url = $(this).attr("data-id");
        $(".loading").addClass('display-block');
        $("#contatos").modal('open');
        $('#contato_result').html('').load(url, function(){
            $(".loading").removeClass('display-block').addClass('display-none')
        });
    });

    $(".endereco").click(function(){
        var url = $(this).attr("data-id");
        $(".loading").addClass('display-block');
        $("#enderecos").modal('open');
        $('#endereco_result').html('').load(url, function(){
            $(".loading").removeClass('display-block').addClass('display-none')
        });
    });
});
