let quantity = 1;
const basePrice = {{post.narxi}};

function increaseQuantity() {
    quantity++;
    updateAmountAndQuantity();
}

function decreaseQuantity() {
    if (quantity > 1) {
        quantity--;
        updateAmountAndQuantity();
    }
}

function updateAmountAndQuantity() {
    const totalAmount = basePrice * quantity;
    document.getElementById("quantity").innerText = ${quantity} dona;
    document.getElementById("amount").value = formatNumber(totalAmount) + ' UZS';
}

function formatNumber(num) {
    return num.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}