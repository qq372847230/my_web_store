$(function(){   // 在页面加载的时候进行具体验证的实现
    set_csrf_token() // 设置CSRF-Token
    $(registForm).validate({    // 利用JSON结构进行验证规则的定义
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
        messages: {
           "code" : {
               rangelength : "验证码的长度必须是5位"
           }
        } ,
        rules: {        // 定义所有要使用的验证规则
            "uid" : {  // 要验证表单的id名称
                required: true ,  // 该内容不允许为空
            } ,
            "password": {
                required : true
            } ,
            "confirm": {
                required : true ,
                equalTo : "#password"
            } ,
            "code" : {
                required : true ,
                rangelength : [5,5],
                remote : {  // 要发送一个ajax的处理请求
                    url : "/vetify.check" , // 验证码检测的地址
                    type : "post" , // 发送一个post请求
                    dataType : "text" , // 异步返回的数据类型为文本数据
                    data : {    // 设置要发送的内容
                        code : function() {
                            return $("#code").val() ;   // 通过输入组件获取code组件内容
                        },
                        // csrf_token: function() {
                        //     return $("#csrf_token").val() ;   // 通过输入组件获取csrf_token组件内容
                        // }
                    } ,
                    dataFilter : function(data,type) {  // 异步回调处理
                        if (data.trim() == "True") {    // 验证码输入正确
                            return true ;
                        } else {    // 验证码输入错误
                            $("#code").val("") ; // 清空原始的输入内容
                            $("#codeImg").attr("src","/vetify.code?rand=" + Math.random()) ;
                            return false ;
                        }
                    }
                }
            }
        }
    }) ;// 验证函数
})