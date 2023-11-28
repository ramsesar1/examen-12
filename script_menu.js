// Inicializar el objeto para almacenar elementos seleccionados
let selectedItems = JSON.parse(localStorage.getItem('selectedItems')) || {};

// Función para manejar clics en los botones "Agregar"
function addToCart(itemId) {
    // Verificar si el item ya existe en el objeto selectedItems
    if (selectedItems[itemId]) {
        // Si existe, incrementar la cantidad
        selectedItems[itemId]++;
    } else {
        // Si no existe, inicializar la cantidad en 1
        selectedItems[itemId] = 1;
    }

    // Almacenar la lista en el localStorage
    localStorage.setItem('selectedItems', JSON.stringify(selectedItems));
}
