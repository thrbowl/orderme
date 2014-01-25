// Jquery Validate ext
// 手机号码验证
jQuery.validator.addMethod("mobile", function (value, element) {
    var length = value.length;
    var mobile = /^(130|131|132|133|134|135|136|137|138|139|150|153|157|158|159|180|187|188|189)\d{8}$/;
    return this.optional(element) || (length == 11 && mobile.test(value));
}, "请正确填写您的手机号码");

$(function () {
    var validator = $("#form-register").validate({
        rules:{
            username:{
                minlength:6,
                maxlength:32,
                required:true
            },
            password:{
                minlength:6,
                maxlength:32,
                required:true
            },
            password_confirm:{
                required:true,
                equalTo:"#password"
            },
            name:{
                minlength:2,
                maxlength:32
            },
            telephone:{
                mobile:true,
                required:true
            },
            address:{
                minlength:10,
                maxlength:128,
                required:true
            }
        },
        messages:{
            username:{
                required:"还没想好你的用户名么？",
                minlength:"这个用户名有点短哦，至少要6个字符才可以的",
                maxlength:"这样太长了吧，你能记住么，我们记不住哦，请在32个字符以内"
            },
            password:{
                required:"没有密码可不行，不怕别人偷你的酒么?",
                minlength:"太短的密码不安全，要6个字符以上才行啊。",
                maxlength:"你的密码太长了，32个字符还不够么？"
            },
            password_confirm:{
                required:"忘了输入密码了吧?",
                equalTo:"还上面的密码不一样啊，是不是记错了？"
            },
            name:{
                minlength:"你的名字怎么会这么短？两字才可以啊",
                maxlength:"这个名字好像不是中国的，我们只在灯塔市那送酒，请别超过32个字符"
            },
            telephone:{
                mobile:"手机号不对呀，找不到你家门，怎么送酒给你啊？",
                required:"留个电话吧，找不着人不行啊"
            },
            address:{
                minlength:"这个地址感觉不靠谱啊，写详细一点吧，至少10个字吧",
                maxlength:"地址太长了，到火星了，128个字还不够么？",
                required:"把酒送哪去啊？"
            }
        },
        highlight:function (element) {
            $(element).closest('.form-group').removeClass('has-success').addClass('has-error');
        },
        success:function (element) {
            element.closest('.form-group').removeClass('has-error').addClass('has-success');
        }
    });

    var birthpicker = $('#birthday_datepicker').datepicker({
        format:"yyyy-mm-dd",
        language:"zh-CN",
        todayHighlight:true,
        endDate:"0d",
        startDate:"-100y"
    }).on('changeDate', function (e) {
            $('#birthday').val(e.format());
        });
});