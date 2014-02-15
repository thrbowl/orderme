function pay(idx) {
    var amount = $("#" + idx).val();
    alert(amount);
}
function addToCart(idx) {
    var amount = $("#" + idx).val();
    alert(amount);
}
$("#star").raty({
    size: 19,
    score: 3,
    starOn: raty_starOn_img,
    starOff: raty_starOff_img,
    starHalf: raty_starHalf_img
});
$("input[name='spinner']").TouchSpin({
    min: 1,
    max: 99999,
    initval: 1,
    prefix: "<strong>购买数目</strong>："
});