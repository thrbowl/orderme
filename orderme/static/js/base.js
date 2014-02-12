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
            var total = simpleCart.total();
            if (total == 0) {
                $("#simpleCart_action_0").removeClass("hide");
                $("#simpleCart_action_1").addClass("hide");
            } else {
                $("#simpleCart_action_1").removeClass("hide");
                $("#simpleCart_action_0").addClass("hide");
            }
            if (total >= 0 && total < MIN_AMOUNT) {
                $("#simpleCart_total").addClass("badge-danger");
            } else {
                $("#simpleCart_total").removeClass("badge-danger");
            }
        }
    });
});