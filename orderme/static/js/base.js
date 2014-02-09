$(function () {
    simpleCart({
        cartColumns: [
            { attr: "name", label: false },
            { view: function (item) {
                return "<span class=\"badge badge-info\">" + simpleCart.toCurrency(item.get("price")) + "</span>" +
                    "<span class=\"text-muted\"> x" + item.quantity() + "</span>" +
                    "<br><a href='javascript:;' class='simpleCart_remove text-danger'>删除</a>";
            }, attr: 'custom' }
        ],
        cartStyle: "div",
        update: function () {
            if (simpleCart.total() == 0) {
                $("#no_cart_tip").removeClass("hide");
                $("#cart_action").addClass("hide");
            } else {
                $("#cart_action").removeClass("hide");
                $("#no_cart_tip").addClass("hide");
            }
        }
    });
});