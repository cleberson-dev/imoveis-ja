// Espelhamento dos Inputs Texto na Área de Previsão

$(".anunciar-box input[type='text']").bind('focusout', function () {
    let name = $(this).attr("name");
    let valor = $(this).val();

    $("#prev-" + name).text(valor);
 
});



// Espelhamento dos Inputs Numero na Área de Previsão

$(".anunciar-box input[type='number']").bind('focusout', function () {
    let name = $(this).attr("name");
    let valor = $(this).val();

    switch(name) {
        case "area":
        $("#prev-area").text(() => (valor != '') ? valor + "m²" : '');
        break;

        case "vagas_estacionamento":
        $("#prev-vagas_estacionamento").text(() => (valor != '') ? valor + " vagas" : '');
        break;

        case "preco":
        valor = valor.replace(/[\D\s\._\-]+/g, "");
        valor = valor ? parseInt(valor, 10) : 0;
        valor = (valor === 0) ? "" : valor.toLocaleString("en-US");

        $("#prev-preco").text(`R$${valor}`.replace(',', '.'));
        break;

        default:
        $("#prev-" + name).text(valor);
    }

    
});



// Espelhamento do elemento select 'tipo'

$(".anunciar-box select[name='tipo']").bind('focusout', function() {
    let opcao = document.querySelector(".anunciar-box select[name='tipo']").selectedOptions[0];
    opcao = opcao.text;
    $("#prev-tipo").text(opcao);
});



// Espelhamento da imagem de capa

$(".anunciar-box input[name='imagem']").change(function () {
    let arquivo = document.querySelector("input[name='imagem']").files[0];
    let fr = new FileReader();
    fr.readAsDataURL(arquivo);
    fr.onload = () => {
        let novoSrc = fr.result;
        $("#imagem").attr("src", novoSrc);
    };
});



// Espelhar o input de descrição na área de preview

$(".anunciar-box .input-area textarea").keyup(function () {
    function controlLength(elemento) {
        let textLength = elemento.val().length;
        let maxLength = elemento.attr("maxlength") || 300;
        let restante = maxLength - textLength;
        let poucosCaracteres = Math.floor(maxLength * 0.15);

        $(".length-legend").text(`${restante} caracteres restantes`);

        if (restante <= poucosCaracteres) {
            $(".length-legend").css("color", "red");
        } else {
            $(".length-legend").css("color", "#707070");
        }
    }

    let conteudo = $(this).val();
    controlLength($(this));

    let previewArea = $(".anunciar-box .preview-area .descricao p");
    previewArea.text(conteudo);
});
