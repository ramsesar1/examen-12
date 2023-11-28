let selectedItems = JSON.parse(localStorage.getItem('selectedItems')) || {};

const contenedorBlanco = document.getElementById('contenedor-blanco');

function updateCart() {
    contenedorBlanco.innerHTML = "";
    for (const itemId in selectedItems) {
        const itemDiv = document.createElement('div');
        itemDiv.classList.add('item');

        const itemName = getItemNameById(itemId);
        const itemPrice = getItemPriceById(itemId);
        const itemImage = getItemImageById(itemId);

        itemDiv.innerHTML = `
            <div class="item-image">
                <img src="${itemImage}" alt="${itemName}">
            </div>
            <div class="item-info">
                <span>${itemName}</span>
                <span>${itemPrice}</span>
            </div>
            <div class="item-buttons">
                <button class="btn-plus">+</button>
                <span class="item-count">${selectedItems[itemId]}</span>
                <button class="btn-minus">-</button>
            </div>
        `;

        contenedorBlanco.appendChild(itemDiv);
    }

    const clearCartButton = document.createElement('button');
    clearCartButton.innerText = 'Limpiar Carrito';
    clearCartButton.addEventListener('click', clearCart);
    contenedorBlanco.appendChild(clearCartButton);
}

function getItemNameById(itemId) {
    switch (itemId) {
        case 'btn1':
            return 'WAGYU A5';
        case 'btn2':
            return 'REFRESCO';
        case 'btn3':
            return 'PAPAS FRITAS';
        default:
            return 'Producto Desconocido';
    }
}

function getItemPriceById(itemId) {
    return "$100"; 
    }

function getItemImageById(itemId) {
   
    switch (itemId) {
        case 'btn1':
            return 'imagen_wagyu.png';
        case 'btn2':
            return 'imagen_refresco.png';
        case 'btn3':
            return 'imagen_papas.png';
        default:
            return 'imagen_desconocida.png';
    }
}

function clearCart() {
    localStorage.removeItem('selectedItems');
    selectedItems = {};
    updateCart();
}

updateCart();
