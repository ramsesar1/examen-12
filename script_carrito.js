// script_carrito.js
// Recuperar la lista de items seleccionados del localStorage
let selectedItems = JSON.parse(localStorage.getItem('selectedItems')) || {};

// Mostrar la lista en el contenedor blanco
const contenedorBlanco = document.getElementById('contenedor-blanco');

function updateCart() {
    // Limpiar el contenedor y volver a mostrar los items actualizados
    contenedorBlanco.innerHTML = "";
    for (const itemId in selectedItems) {
        const itemDiv = document.createElement('div');
        itemDiv.classList.add('item');

        // Obtener el nombre, precio e imagen del producto por su ID
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

    // Añadir el botón para limpiar el carrito
    const clearCartButton = document.createElement('button');
    clearCartButton.innerText = 'Limpiar Carrito';
    clearCartButton.addEventListener('click', clearCart);
    contenedorBlanco.appendChild(clearCartButton);
}

// Funciones auxiliares para obtener información del producto por su ID
function getItemNameById(itemId) {
    switch (itemId) {
        case 'btn1':
            return 'WAGYU A5';
        case 'btn2':
            return 'REFRESCO';
        case 'btn3':
            return 'PAPAS FRITAS';
        // Agrega más casos según tus botones
        default:
            return 'Producto Desconocido';
    }
}

function getItemPriceById(itemId) {
    // Lógica para obtener el precio del producto por su ID
    return "$100"; // Ejemplo de precio
}

function getItemImageById(itemId) {
    // Lógica para obtener la imagen del producto por su ID
    // Puedes retornar la ruta a la imagen correspondiente a cada producto
    // Aquí debes agregar más casos según tus botones
    switch (itemId) {
        case 'btn1':
            return 'imagen_wagyu.png';
        case 'btn2':
            return 'imagen_refresco.png';
        case 'btn3':
            return 'imagen_papas.png';
        // Agrega más casos según tus botones
        default:
            return 'imagen_desconocida.png';
    }
}

// Función para eliminar todos los elementos del carrito y del localStorage
function clearCart() {
    localStorage.removeItem('selectedItems');
    selectedItems = {};
    updateCart();
}

// Mostrar la lista al cargar la página
updateCart();
