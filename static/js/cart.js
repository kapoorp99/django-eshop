if(localStorage.getItem('cart') == null)
{
    var cart = {};
}
else
{
    cart = JSON.parse(localStorage.getItem('cart'));
    document.getElementById('cart').innerHTML = Object.keys(cart).length;
}
$('.cart').click(function(){
var products_id = this.id.toString();
if(cart[products_id] != undefined)
{
    cart[products_id] = cart[products_id] + 1;
}
else
{
    cart[products_id] = 1
}
localStorage.setItem('cart',JSON.stringify(cart));
document.getElementById('cart').innerHTML = Object.keys(cart).length;
});
$('#cart_popover').popover();
document.getElementById("cart_popover").setAttribute('data-content','<p>Products content</p>');