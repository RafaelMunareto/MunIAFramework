
$(document).ready(function(){

    var posicao = localStorage.getItem('posicaoScroll');

    if(posicao) {

        setTimeout(function() {

            window.scrollTo(0, posicao);

        }, 0);

    }

    window.onscroll = function (e) {

        posicao = window.scrollY;

        localStorage.setItem('posicaoScroll', JSON.stringify(posicao));

    }
});
    