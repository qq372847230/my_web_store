$(function(){   // 在页面加载的时候进行具体验证的实现
    set_csrf_token() // 设置CSRF-Token
    $(birthday).datetimepicker({
		language: "zh-CN", 	// 中文资源文件
		weekStart: 1,		// 一周从哪一天开始 0表示星期天
	    todayBtn:  true,		// 日期时间选择器组件的底部显示一个 "Today" 按钮用以选择当前日期。
	    autoclose: true, 		// 当选择一个日期之后是否立即关闭此日期时间选择器。
	    todayHighlight: 1,	// 如果为true, 高亮当前日期
	    startView: 2, 		// 日期时间选择器打开之后首先显示的视图。 2 or 'month' for month view (the default)
	    forceParse: 1,		// 当选择器关闭的时候，是否强制解析输入框中的值。
	    showMeridian: 1 , 	// 选项里是否有天或小时
	    minView: "month" , 	// 选择日期后，不会再跳转去选择时分秒
	    format: 'yyyy-mm-dd'
    });
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
            "name" : {  // 要验证表单的id名称
                required: true ,  // 该内容不允许为空
            } ,
            "gender": {
                required : true
            } ,
            "photo": {
                extension : ["jpg","png","gif","bmp"]
            } ,
            "birthday": {
                required : true ,
                dateISO: true
            } ,
            "note": {
                required : true
            }
        }
    }) ;// 验证函数
    CKEDITOR.replace("note");
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