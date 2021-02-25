$(function () {
    set_csrf_token() // 设置CSRF-Token
    $(goodsForm).validate({    // 利用JSON结构进行验证规则的定义
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
            "name" : {  // 要验证表单的id名称
                required: true ,  // 该内容不允许为空
            } ,
            "price": {
                required : true,
                number: true
            } ,
            "iid": {
                required: true
            } ,
            "file": {
                extension : ["jpg","png","gif","bmp"]
            }
        }
    }) ;// 验证函数
    CKEDITOR.replace("content");
    CKEDITOR.editorConfig = function (config) {
    // Define changes to default configuration here. For example:
    // config.language = 'fr';
    // config.uiColor = '#AADC6E';
    config.toolbarGroups = [
        {name: 'clipboard', groups: ['clipboard', 'undo']},
        {name: 'editing', groups: ['find', 'selection', 'spellchecker', 'editing']},
        {name: 'forms', groups: ['forms']},
        {name: 'basicstyles', groups: ['basicstyles', 'cleanup']},
        {name: 'paragraph', groups: ['list', 'indent', 'blocks', 'align', 'bidi', 'paragraph']},
        {name: 'links', groups: ['links']},
        {name: 'insert', groups: ['insert']},
        {name: 'styles', groups: ['styles']},
        {name: 'colors', groups: ['colors']},
        {name: 'document', groups: ['document', 'doctools', 'mode']},
        {name: 'tools', groups: ['tools']},
        {name: 'others', groups: ['others']},
        {name: 'about', groups: ['about']}
    ];

    //移除的按钮
    config.removeButtons = 'Templates,Print,Find,Replace,SelectAll,Scayt,Checkbox,Form,Radio,TextField,Textarea,Select,Button,ImageButton,HiddenField,CreateDiv,Blockquote,BidiLtr,BidiRtl,Flash,PageBreak,Iframe,About,ShowBlocks,Smiley,SpecialChar,HorizontalRule,CopyFormatting,RemoveFormat';

    //上传图片窗口用到的接口
    config.filebrowserImageUploadUrl = "http://localhost/back/admin/common/upload.action";
    config.filebrowserUploadUrl = "http://localhost/back/admin/common/upload.action";

    // 使上传图片弹窗出现对应的“上传”tab标签
    config.removeDialogTabs = 'image:advanced;link:advanced';

    //粘贴图片时用得到
    config.extraPlugins = 'uploadimage';
    config.uploadUrl = 'http://localhost/back/admin/common/upload.action';
};
})
