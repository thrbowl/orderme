/* Jquery Validate ext
 * 手机号码验证
 */
jQuery.validator.addMethod("mobile", function (value, element) {
    var length = value.length;
    var mobile = /^(130|131|132|133|134|135|136|137|138|139|150|153|157|158|159|180|187|188|189)\d{8}$/;
    return this.optional(element) || (length == 11 && mobile.test(value));
}, "请正确填写您的手机号码");

$(function () {
    var validator = $("#form-register").validate({
        rules: {
            username: {
                minlength: 6,
                maxlength: 32,
                required: true,
                remote: remote_url
            },
            password: {
                minlength: 6,
                maxlength: 32,
                required: true
            },
            password_confirm: {
                required: true,
                equalTo: "#password"
            },
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
            username: {
                required: "还没想好用户名么？",
                minlength: "这个用户名有点短，至少要6个字",
                maxlength: "这个用户名太长了，不要超过32个字",
                remote: "不好意思，这个用户名已经被别人抢走了，请重新输入"
            },
            password: {
                required: "密码是必须的",
                minlength: "太短的密码不安全，至少要6个字",
                maxlength: "这个密码太长了，不要超过32个字"
            },
            password_confirm: {
                required: "请确认一下上面输入的密码",
                equalTo: "和上面的密码不一样，是不是记错了？"
            },
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