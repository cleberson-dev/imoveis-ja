
window.addEventListener('load', formatarReal);




function formatarReal(e) {
    let precoElementos = document.querySelectorAll('.preco-format');

    for (let precoElemento of precoElementos) {
        let preco = precoElemento.innerHTML;

        preco = preco.replace(',0', '');

        let options = {
            style: 'currency', 
            currency: 'BRL', 
            currencyDisplay: "symbol"
        };

        preco = parseInt(preco, 10).toLocaleString('pt-BR', options);

        precoElemento.innerHTML = preco;

    }

}