/* Jquery Validate ext
 * 手机号码验证
 */
jQuery.validator.addMethod("mobile", function (value, element) {
    var length = value.length;
    var mobile = /^(130|131|132|133|134|135|136|137|138|139|150|153|157|158|159|180|187|188|189)\d{8}$/;
    return this.optional(element) || (length == 11 && mobile.test(value));
}, "请正确填写您的手机号码");

$(function () {
    simpleCart({
        cartColumns:[
            { attr:"custom-name", label:"商品", view:function (item) {
                return '<a href="#">' + item.get("name") + '</a><input type="hidden" name="idxs" value="' + item.get("idx") + '">';
            }},
            { attr:"price", label:"单价", view:"currency"},
            { attr:"custom-quantity", label:"数量", view:function (item) {
                return '<div class="input-group input-group-sm item-quantity">' +
                    '<span class="input-group-btn">' +
                    '<button class="btn btn-default simpleCart_decrement" type="button">-</button>' +
                    '</span>' +
                    '<input type="text" name="' + item.get("idx") + '_quantity" class="input-sm form-control simpleCart_input" value="' + item.quantity() + '">' +
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
                $("#glyphicon_warning_sign").removeClass("hide");
                $("#checkout_submit").prop( "disabled", true );
            } else {
                $("#glyphicon_warning_sign").addClass("hide");
                $("#checkout_submit").prop( "disabled", false );
            }
        }
    });

    var validator = $("#form-checkout").validate({
        rules: {
            name: {
                required: true,
                minlength: 2,
                maxlength: 32
            },
            mobile: {
                mobile: true,
                required: true
            },
            address: {
                minlength: 7,
                maxlength: 255,
                required: true
            }
        },
        messages: {
            name: {
                required: "请问您怎么称呼呢？",
                minlength: "这个称呼太短了，至少要2个字",
                maxlength: "这个称呼太长了，不要超过32个字"
            },
            mobile: {
                mobile: "手机号不正确，检查一下吧",
                required: "留个手机号吧，不然找不到人了"
            },
            address: {
                minlength: "地址写详细一点吧，至少7个字",
                maxlength: "地址太长了，到火星了，不要超过255个字",
                required: "留个地址吧，不让把酒送哪去呢？"
            }
        },
        highlight: function (element) {
            $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
        },
        success: function (element) {
            element.closest('.form-group').removeClass('has-error').addClass('has-success');
        }
    });
});