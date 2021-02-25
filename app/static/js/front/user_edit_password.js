$(function(){   // 在页面加载的时候进行具体验证的实现
    set_csrf_token() // 设置CSRF-Token
    $(userForm).validate({    // 利用JSON结构进行验证规则的定义
        highlight: function(element,errorClass) { // 进行高亮显示的配置
            $(element).attr("class","form-control is-invalid") ; // 设置错误信息的样式
        },
        unhighlight : function(element,errorClass) {
            $(element).attr("class","form-control is-valid") ; // 设置错误信息的样式
        } ,
        errorPlacement : function(error,element) {
            elementId = $(element).attr("id") ; // 获取元素的id
            if (elementId.indexOf(".")) {
                elementId = elementId.replace(".","\\.") ; // 进行“.”的替换
            }
            msgId = elementId + "Msg" ; // 获取错误文本的显示元素
            $("#" + msgId).empty() ; // 清空已有内容
            $(error).attr("class","text-danger") ;
            $("#" + msgId).append(error) ; // 追加错误信息
        } ,
        success : function(error,element) {  // 操作成功
            elementId = $(element).attr("id") ; // 获取元素的id
            if (elementId.indexOf(".")) {
                elementId = elementId.replace(".","\\.") ; // 进行“.”的替换
            }
            msgId = elementId + "Msg" ; // 获取错误文本的显示元素
            $("#" + msgId).empty() ; // 清空已有内容
            $("#" + msgId).append("<span class='h2'><span class='text-success glyphicon glyphicon-ok'/></span>") ; // 追加错误信息
        } ,
        rules: {        // 定义所有要使用的验证规则
            "oldpwd" : {  // 要验证表单的id名称
                required: true ,  // 该内容不允许为空
            } ,
            "password": {
                required : true
            } ,
            "confirm": {
                required : true ,
                equalTo : "#password"
            }
        }
    }) ;// 验证函数
})