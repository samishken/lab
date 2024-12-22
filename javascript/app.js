let totalPrice = 19;
let shippingCost;
console.log(totalPrice)

if (totalPrice <= 10) {
    shippingCost = 5
} else if (totalPrice <= 20) {
    shippingCost = 3
} else if (totalPrice > 20) {
    shippingCost = 4
} else {
    shippingCost = 0
}

