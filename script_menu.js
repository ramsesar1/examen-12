let selectedItems = JSON.parse(localStorage.getItem('selectedItems')) || {};

function addToCart(itemId) {
    if (selectedItems[itemId]) {
        selectedItems[itemId]++;
    } else {
        selectedItems[itemId] = 1;
    }

    localStorage.setItem('selectedItems', JSON.stringify(selectedItems));
}
