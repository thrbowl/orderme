$(function () {
    simpleCart({
        cartColumns:[
            { attr:"custom-name", label:"商品", view:function (item) {
                return '<a href="#">' + item.get("name") + '</a><input type="hidden" name="item_idx" value="' + item.get("idx") + '">';
            }},
            { attr:"price", label:"单价", view:"currency"},
            { attr:"custom-quantity", label:"数量", view:function (item) {
                return '<div class="input-group input-group-sm item-quantity">' +
                    '<span class="input-group-btn">' +
                    '<button class="btn btn-default simpleCart_decrement" type="button">-</button>' +
                    '</span>' +
                    '<input type="text" name="item_quantity" class="input-sm form-control simpleCart_input" value="' + item.quantity() + '">' +
                    '<span class="input-group-btn">' +
                    '<button class="btn btn-default simpleCart_increment" type="button">+</button>' +
                    '</span>' +
                    '</div>';
            }},
            { attr:'custom-remove', view:function () {
                return '<button type="button" class="simpleCart_remove btn btn-xs">删&nbsp;除</button>';
            }}
        ],
        cartStyle:"table",
        update:function () {

        }
    });
});