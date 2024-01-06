   
  $(document).ready(() => {
    $("input[name='cep']").mask('99999-999');
    
    let formClear = () => {
        // Limpa valores do formulário de cep.
        $("input[name='endereco']").val("");
        $("input[name='bairro']").val("");
        $("input[name='cidade']").val("");
        $("input[name='estado']").val("");
    }
    
    //Quando o campo cep perde o foco.
    $("input[name='cep']").blur(() => {

        //Nova variável "cep" somente com dígitos.
        let zipCode =  $("input[name='cep']").val().replace(/\D/g, '');

        //Verifica se campo cep possui valor informado.
        if (zipCode != "") {

            //Expressão regular para validar o CEP.
            let validCep = /^[0-9]{8}$/;

            //Valida o formato do CEP.
            if(validCep.test(zipCode)) {

                //Preenche os campos com "..." enquanto consulta webservice.
                $("#rua").val("...");
                $("#bairro").val("...");
                $("#cidade").val("...");
                $("#uf").val("...");
                $("#ibge").val("...");
                
                //Consulta o webservice viacep.com.br/
                $.getJSON(`https://viacep.com.br/ws/${zipCode}/json/?callback=?`, data => {

                    if (!("erro" in data)) {
                        //Atualiza os campos com os valores da consulta.
                        $("input[name='endereco']").val(data.logradouro);
                        $("input[name='bairro']").val(data.bairro);
                        $("input[name='cidade']").val(data.localidade);
                        $("input[name='estado']").val(data.uf);
                    } //end if.
                    else {
                        //CEP pesquisado não foi encontrado.
                        formClear();
                        alert("CEP não encontrado.");
                    }
                });
            } //end if.
            else {
                //cep é inválido.
                formClear();
                alert("Formato de CEP inválido.");
            }
        } //end if.
        else {
            //cep sem valor, limpa formulário.
            formClear();
        }
    });
});