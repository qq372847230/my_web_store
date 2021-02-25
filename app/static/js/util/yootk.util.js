/**
 * 警告框操作信息，ID必须为“alertDiv”
 * @param flag 操作成功或失败的标记
 * @param suctext 操作成功时的显示文本内容
 * @param faltext 操作失败时的显示文本内容
 */
function operateAlert(flag,suctext,faltext) {
	if (flag) {
		$("#alertDiv").attr("class","alert alert-success") ;
		$("#alertText").text(suctext) ;
	} else {
		$("#alertDiv").attr("class","alert alert-danger") ;
		$("#alertText").text(faltext) ;
	}
	$("#alertDiv").fadeIn(1000,function(){
        $("#alertDiv").fadeOut(3000) ;
    }) ;
}

function set_csrf_token() {
	var csrftoken = $('meta[name=csrf-token]').attr('content')
	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken)
			}
		}
	})
}
