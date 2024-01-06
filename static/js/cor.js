$(document).ready(function(){

	$(".cor").each(function(){
		if($(this).text() >= 100){  
			$(this).addClass('cem');
		}else if ($(this).text() >=95 && $(this).text() < 100 ) {
			$(this).addClass('noventa');	
		}else if ($(this).text() >=90 && $(this).text() < 95){
			$(this).addClass('oitenta');
		}else if($(this).text() < 90){
			$(this).addClass('setenta');
		}
	});

	$(".cor_float").each(function(){
		var valor = $(this).text().replace(",", ".");
		if(valor >= 100){  
			$(this).addClass('cem');
		}else if (valor >=95 && valor < 100 ) {
			$(this).addClass('noventa');	
		}else if (valor>=90 && valor < 95){
			$(this).addClass('oitenta');
		}else if(valor < 90){
			$(this).addClass('setenta');
		}
	});
	
	$(".cor_back").each(function(){
		if($(this).text() >= 100){  
			$(this).addClass('cem_back');
		}else if ($(this).text() >=95 && $(this).text() < 100 ) {
			$(this).addClass('noventa_back');	
		}else if ($(this).text() >=90 && $(this).text() < 95){
			$(this).addClass('oitenta_back');
		}else if($(this).text() < 90){
			$(this).addClass('setenta_back');
		}
	});

	$(".cor").each(function(){
		if($(this).text() >= 100){  
			$(this).addClass('cem');
		}else if ($(this).text() >=95 && $(this).text() < 100 ) {
			$(this).addClass('noventa');	
		}else if ($(this).text() >=90 && $(this).text() < 95){
			$(this).addClass('oitenta');
		}else if($(this).text() < 90){
			$(this).addClass('setenta');
		}
	});

	/* Table agendamento para mudar cor das consultas */
	
	$("#table_agendamento .tipo").each(function(){
		var tipo = $(this).text();
		if(tipo == 'BANHO E TOSA'){
			$(this).parent().addClass('cor_tr_purple')
		}else if (tipo == 'CIRURGIA'){
			$(this).parent().addClass('cor_tr_red')
		}else if (tipo == 'CONSULTA'){
			$(this).parent().addClass('cor_tr_teal')
		}else if (tipo == 'RETORNO'){
			$(this).parent().addClass('cor_tr_cyan')
		}else if (tipo == 'VACINA'){
			$(this).parent().addClass('cor_tr_yellow')
		}
	});

});
