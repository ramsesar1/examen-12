const historial = JSON.parse(localStorage.getItem('historial')) || [];

const contenedorBlanco = document.getElementById('contenedor-blanco');

function mostrarHistorial() {
    contenedorBlanco.innerHTML = "";
    historial.forEach((compra, index) => {
        const listItem = document.createElement('div');
        listItem.classList.add('historial-item');
        listItem.innerHTML = `
            <div class="historial-header">Compra ${index + 1}</div>
            <div class="historial-details">
                ${Object.keys(compra).map(itemId => `
                    <div class="historial-item-details">
                        <span>${getItemNameById(itemId)}</span>
                        <span>${getItemPriceById(itemId)}</span>
                        <span>${compra[itemId]} unidades</span>
                    </div>
                `).join('')}
            </div>
        `;
        contenedorBlanco.appendChild(listItem);
    });
}

function getItemNameById(itemId) {
    switch (itemId) {
        case 'btn1':
            return 'WAGYU A5';
        case 'btn2':
            return 'REFRESCO';
        case 'btn3':
            return 'PAPAS FRITAS';
        case 'btn4':
            return 'PACK INDIVIDUAL';
        case 'btn8':
            return 'PRIME';
        case 'btn7':
            return 'GUACA-BACCON';
        case 'btn6':
            return 'LOW-CARB';
        case 'btn5':
            return 'PACK-4-FAMILY';
        default:
            return 'Producto Desconocido';
    }
}

function getItemPriceById(itemId) {
    switch (itemId) {
        case 'btn1':
            return '$1250';
        case 'btn2':
            return '$25';
        case 'btn3':
            return '$50';
        case 'btn4':
            return '$160';
        case 'btn8':
            return '$450';
        case 'btn7':
            return '$120';
        case 'btn6':
            return '$130';
        case 'btn5':
            return '$250';
        default:
            return '$0';
    }
}

mostrarHistorial();
