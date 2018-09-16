// CUSTOMIZAÇÃO DO SELECT DAS TAGS DOS  IMÓVEIS COM ESPELHAMENTO NA TELA DE PREVISÃO

// Definindo o container principal e o elemento select a personalizar.
let rootContainer = document.querySelector('.tag-select');
let selectElement = rootContainer.getElementsByTagName("select")[0];

let options = selectElement.options;

for (let option of options) {
    let text = option.innerHTML;
    let selected = option.selected;
    let value = option.value; 

    optionElement = document.createElement("div");
    optionElement.classList.add("option");
    optionElement.innerHTML = text;

    if (selected) { 
        createPreviewItem();
        optionElement.classList.add("checked"); 
    }

    optionElement.addEventListener("click", function() {
        option.selected = !option.selected;
        if (option.selected) {
            createPreviewItem();
            this.classList.add("checked");
        } else {
            removePreviewItem(value);
            this.classList.remove("checked");
        }
    });

    rootContainer.appendChild(optionElement);
    
    
    function createPreviewItem() {
        let previewArea = document.querySelector(".preview-area .tags-content");
        let previewItem = document.createElement("div")
        previewItem.innerHTML = text;
        previewItem.classList.add("prev-tag");
        previewItem.setAttribute("data-value", value);
        previewArea.appendChild(previewItem);
    }
    function removePreviewItem(value) {
        let item = document.querySelector(`.tags-content .prev-tag[data-value='${value}']`);
        item.remove();
    }
}

