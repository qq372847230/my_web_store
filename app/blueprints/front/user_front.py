from flask import Blueprint, session, render_template, request, make_response
from app.mapping.orm import User
from app.util.factory import get_service_instance
from app.util.reflect import get_instance_object # 反射进行对象实例化处理
from app.util.yootk_common import upload_file, get_md5_code, get_param_value, cookie_clear
user_front_bp = Blueprint(name="user_front", import_name=__name__) # 前台用户蓝图
@user_front_bp.route("/edit_password.page")
def user_edit_password_page(): # 修改密码页面
    return render_template("/front/admin/user/user_edit_password.html")
@user_front_bp.route("/edit_password.action", methods=["POST"])
def user_edit_password_handle():
    user = User(uid=session.get("uid"), password=get_md5_code(get_param_value("oldpwd")))
    message = "用户密码修改失败，请确认原始密码是否输入正确，为了您的账户安全请重新登录！"
    url = "/login.page" # 回到登录页
    if get_service_instance("UserService").edit_password(user, get_md5_code(get_param_value("password"))): # 业务修改
        message = "密码修改成功，为了您的账户安全，请重新登录系统！"
    session.clear() # 清空session
    response = make_response(render_template("common/forward.html", message=message, url=url))
    cookie_clear(response)
    return response

@user_front_bp.route("/edit.page")
def user_edit_page(): # 页面跳转
    uid = session.get("uid") # 获取保存的uid数据
    return render_template("/front/admin/user/user_edit.html", user=get_service_instance("UserSignService").get_user(uid))
@user_front_bp.route("/edit.action", methods=["POST"])
def user_edit_handle():
    user = get_instance_object(User) # 反射接收数据
    user.uid = session.get("uid") # 更新的用户ID
    user.photo = upload_file(request.files.get("file"), filename=user.photo, default_filename="user-nophoto.png")
    message = "用户信息修改失败， 请重新确认您输入的信息是否正确！"
    url = "/front/admin/user/edit.page"
    if get_service_instance("UserService").edit_user(user): # 业务更新
        session["photo"] = user.photo # 更换图片名称
        message = "用户休息修改成功！"
    return render_template("common/forward.html", message=message, url=url)