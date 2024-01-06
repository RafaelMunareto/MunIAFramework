

 $(document).ready(function(){

    $('.sidenav').sidenav({
        edge: 'right'
    });

    $('.dropdown-trigger').dropdown();

	setInterval(function() {
    	$('.carousel').carousel('next')
    }, 3000);

    $('.carousel').carousel({
        indicators: false
    });

     
    $('.modal').modal();
    /*
    $('.modal-trigger').click(function(){ 
        var url = $('.modal-trigger').attr("data-source"); 
        
        $('.modal-ok').click(function() {
            $(location).attr('href',url);
        })       
    });*/
    
    $('.comite_select').formSelect();
    $('.esteira_lot').formSelect();
    $('.money').mask("#.##0,00", {reverse: true});
    $('.inteiro').mask("#.##0", {reverse: true});
    $('.date').mask('00/00/0000');
    $('.cpf').mask('000.000.000-00', {reverse: true});
    $('.cnpj').mask('00.000.000/0000-00', {reverse: true});
    $('.telefone').mask('(00) 0000-0000');
    $('.celular').mask('(00) 00000-0000');
    $('.cep').mask('00000-000');
    $('.email').mask("A", {
        translation: {
            "A": { pattern: /[\w@\-.+]/, recursive: true }
        }
    });

    if ($('#message').text() !==''){
        $('#titulo').addClass('display-none')
        setInterval(function(){
            $('#message').addClass('display-none')
            $('#titulo').addClass('display-block animated flipInX')
        }, 3000);
    }
   
    $('#id_prescricao').show(function(){
        $(this).css("height","200px");
    });

    $('.buttonPreloader').click(function(){
        $('.preloader').removeClass('display-none');
    });

    $('.timepicker').timepicker({
        twelveHour:false,
        i18n:{
            cancel: 'Cancelar',
            done: 'OK'
        },
        vibrate:false
    });
   

    $('.datepicker').datepicker({
        format:'yyyy-mm-dd',
        i18n:{
            months: ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'],
            monthsShort: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
            weekdays: ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo'],
            weekdaysAbbrev: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
            weekdaysShort: ['Dom', 'Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab'],
            today: 'Hoje',
            clear: 'Limpar',
            close: 'Pronto',
            labelMonthNext: 'Próximo mês',
            labelMonthPrev: 'Mês anterior',
            labelMonthSelect: 'Selecione um mês',
            labelYearSelect: 'Selecione um ano',
            selectMonths: true,
            selectYears: 15,
            cancel: 'Cancelar',
            clear: 'Limpar'
        }
      })

      $(".cpf_cnpj").keypress(function(){
        var cnpjcpf= $(this).val().length;
        if(cnpjcpf <= '13'){
            $('.cpf_cnpj').mask('000.000.000-00', {reverse: true});
        } else if (cnpjcpf > '13'){
            $('.cpf_cnpj').mask('00.000.000/0000-00', {reverse: true});
        }else {
            $('.cpf_cnpj').mask('000.000.000-00', {reverse: true});
        }                 
    });

 
});


