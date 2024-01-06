
$(document).ready(function(){

    $('#table_top').DataTable({
        "language": {
            "paginate": {
              "previous": "Anterior",
              "next": "Próximo",
            },
            "lengthMenu": "",
            "zeroRecords": "Não foi encontrado - desculpe",
            "info": "Mostrando pag _PAGE_ de _PAGES_",
            "infoEmpty": "Nenhum registro válido",
            "infoFiltered": "(filtrado de _MAX_ total de registros.)",
            "search": "Procurar"

          }
    });


    $('#table_top2').DataTable({
        "language": {
            "paginate": {
              "previous": "Anterior",
              "next": "Próximo",
            },
            "lengthMenu": "",
            "zeroRecords": "Não foi encontrado - desculpe",
            "info": "Mostrando pag _PAGE_ de _PAGES_",
            "infoEmpty": "Nenhum registro válido",
            "infoFiltered": "(filtrado de _MAX_ total de registros.)",
            "search": "Procurar"

          },

    });

    $('#table_segmentos').DataTable({
        "language": {
            "paginate": {
              "previous": "Anterior",
              "next": "Próximo",
            },
            "lengthMenu": "",
            "zeroRecords": "Não foi encontrado - desculpe",
            "info": "Mostrando pag _PAGE_ de _PAGES_",
            "infoEmpty": "Nenhum registro válido",
            "infoFiltered": "(filtrado de _MAX_ total de registros.)",
            "search": "Procurar"

          }
    });

    $('#table_campanha').DataTable({
        "order": [[ 9, "desc" ]],
        "language": {
            "paginate": {
              "previous": "Anterior",
              "next": "Próximo",
            },
            "lengthMenu": "",
            "zeroRecords": "Não foi encontrado - desculpe",
            "info": "Mostrando pag _PAGE_ de _PAGES_",
            "infoEmpty": "Nenhum registro válido",
            "infoFiltered": "(filtrado de _MAX_ total de registros.)",
            "search": "Procurar"

          }
    });

    $('#table_seguridade').DataTable({
        "order": [[ 7, "desc" ]],
        "language": {
            "paginate": {
              "previous": "Anterior",
              "next": "Próximo",
            },
            "lengthMenu": "",
            "zeroRecords": "Não foi encontrado - desculpe",
            "info": "Mostrando pag _PAGE_ de _PAGES_",
            "infoEmpty": "Nenhum registro válido",
            "infoFiltered": "(filtrado de _MAX_ total de registros.)",
            "search": "Procurar"

          }
    });



    $('#controle_acesso').DataTable({
      "order": [[ 0, "desc" ]],
      "language": {
          "paginate": {
            "previous": "Anterior",
            "next": "Próximo",
          },
          "lengthMenu": "",
          "zeroRecords": "Não foi encontrado - desculpe",
          "info": "Mostrando pag _PAGE_ de _PAGES_",
          "infoEmpty": "Nenhum registro válido",
          "infoFiltered": "(filtrado de _MAX_ total de registros.)",
          "search": "Procurar"

        }
  });

  $('#gov').DataTable({
    "order": [[ 2, "desc" ]],
    "language": {
        "paginate": {
          "previous": "Anterior",
          "next": "Próximo",
        },
        "lengthMenu": "",
        "zeroRecords": "Não foi encontrado - desculpe",
        "info": "Mostrando pag _PAGE_ de _PAGES_",
        "infoEmpty": "Nenhum registro válido",
        "infoFiltered": "(filtrado de _MAX_ total de registros.)",
        "search": "Procurar"

      }
});

$('#table_comite').DataTable({
  "order": [[ 10, "asc" ]],
  "language": {
      "paginate": {
        "previous": "Anterior",
        "next": "Próximo",
      },
      "lengthMenu": "",
      "zeroRecords": "Não foi encontrado - desculpe",
      "info": "Mostrando pag _PAGE_ de _PAGES_",
      "infoEmpty": "Nenhum registro válido",
      "infoFiltered": "(filtrado de _MAX_ total de registros.)",
      "search": "Procurar"

    }
});


$('#table_folhas').DataTable({
  "order": [[ 13, "asc" ]],
  "language": {
      "paginate": {
        "previous": "Anterior",
        "next": "Próximo",
      },
      "lengthMenu": "",
      "zeroRecords": "Não foi encontrado - desculpe",
      "info": "Mostrando pag _PAGE_ de _PAGES_",
      "infoEmpty": "Nenhum registro válido",
      "infoFiltered": "(filtrado de _MAX_ total de registros.)",
      "search": "Procurar"

    }
});



$('#table_ferias').DataTable({
  "order": [[ 5, "asc" ]],
  "language": {
      "paginate": {
        "previous": "Anterior",
        "next": "Próximo",
      },
      "lengthMenu": "",
      "zeroRecords": "Não foi encontrado - desculpe",
      "info": "Mostrando pag _PAGE_ de _PAGES_",
      "infoEmpty": "Nenhum registro válido",
      "infoFiltered": "(filtrado de _MAX_ total de registros.)",
      "search": "Procurar"

    }
});



});


