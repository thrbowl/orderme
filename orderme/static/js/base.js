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
                $("#simpleCart_items").addClass("hide");
                $("#simpleCart_no_items").removeClass("hide");
                $("#simpleCart_action").addClass("hide");
            } else {
                $("#simpleCart_items").removeClass("hide");
                $("#simpleCart_no_items").addClass("hide");
                $("#simpleCart_action").removeClass("hide");
            }
            if (total >= 0 && total < MIN_AMOUNT) {
                $("#glyphicon_warning_sign_1").removeClass("hide");
                $("#glyphicon_warning_sign_2").removeClass("hide");
            } else {
                $("#glyphicon_warning_sign_1").addClass("hide");
                $("#glyphicon_warning_sign_2").addClass("hide");
            }
        }
    });
});