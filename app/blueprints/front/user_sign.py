from flask import Blueprint
from flask import render_template, make_response
from flask import session
from app.mapping.orm import User
from app.util.yootk_common import get_md5_code, get_param_value, cookie_set, cookie_clear
from app.util.reflect import get_instance_object # 反射进行对象实例化处理
user_sign_bp = Blueprint(name="user_sign", import_name=__name__)
from app.util.factory import get_service_instance
@user_sign_bp.route("/regist.action", methods=["POST"])
def regist_handle():
    service = get_service_instance("UserSignService")  # 获取业务层对象实例
    user = get_instance_object(User) # 反射操作
    user.password = get_md5_code(user.password) # 接收password的参数
    message = "用户注册失败，请检查用户名是否可用！" # 默认的提示信息
    url = "/regist.page" # 默认的跳转路径
    if service.add_user(user): # 用户增加业务
        session["uid"] = user.uid  # 保存用户id
        session["photo"] = "user-nophoto.png"  # 用户的照片保存在数据库里面
        session["admin"] = 0  # 管理员标记
        message = "用户注册成功，即将回到沐言优拓站点的首页！"
        url = "/"
    return render_template("common/forward.html", message=message, url=url)

@user_sign_bp.route("/login.page")
def login_page():
    return render_template("/front/user_login.html")
@user_sign_bp.route("/login.action", methods=["POST"])
def login_handle():
    service = get_service_instance("UserSignService")  # 获取业务层对象实例
    user = get_instance_object(User)  # 反射操作
    user.password = get_md5_code(user.password)  # 接收password的参数
    message = "用户登录失败，错误的用户名或密码！"  # 默认的提示信息
    url = "/login.page" # 登录失败返回到登录页面
    result_user = service.login(user) # 调用登录业务
    if result_user: # 登录成功了
        # 考虑到用户界面的显示控制，这个地方一定要为其追加有相应的session数据配置
        session["uid"] = user.uid # 保存用户id
        session["photo"] = result_user.photo # 用户的照片保存在数据库里面
        session["admin"] = result_user.admin # 管理员标记
        message = "用户登录成功，欢迎%s光临。" % user.uid  # 默认的提示信息
        url = "/" # 回到首页
        response = make_response(render_template("common/forward.html", message=message, url=url))
        rememberme = get_param_value("rememberme")  # 获取免登录的配置
        if rememberme and "True" == rememberme:  # 已经被选中了
            cookie_set(response, "yootk-user", "%s" % user.uid)  # 进行Cookie记录
        return response
    else:
        return render_template("common/forward.html", message=message, url=url)
@user_sign_bp.route("/regist.page")
def regist_page():
    return render_template("/front/user_regist.html")
@user_sign_bp.route("/logout.action")
def logout_handle(): # 注销处理
    session.clear() # 清除全部的session数据
    message = "用户注销成功，您已安全退出，欢迎下次再来！"
    url = "/"
    response = make_response(render_template("common/forward.html", message=message, url=url))
    cookie_clear(response)
    return response