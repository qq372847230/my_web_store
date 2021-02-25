from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from app.util.yootk_common import parse, cookie_get
from app.util.factory import get_service_instance
import flask, traceback
import os # 需要进行所有的文件路径的操作
from app.util.validate import validate_request_param
VALIDATIONS_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "validations.properties")
MESSAGES_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "messages.properties")
messages_properties = parse(MESSAGES_PATH) # 根据路径解析资源
validations_properties = parse(VALIDATIONS_PATH) # 根据路径解析资源
database = SQLAlchemy() # 创建FLask-SQLAlchemy对象
def config_extensions(app): # 配置初始化
    database.init_app(app)

def config_filter(app): # 配置过滤器
    @app.template_filter("selected")
    def checked_handle(value, data): # data就是传入的数值
        if data == value:
            return "selected"
        return ""

    @app.template_filter("checked")
    def checked_handle(value, data):  # data就是传入的数值
        if data == value:
            return "checked"
        return ""

    @app.template_filter("active")
    def active_handle(value, data):
        if value == data:
            return "active"
        return ""

    @app.template_filter("disabled")
    def disabled_handle(value, data):
        if value == data:
            return "disabled"
        return ""

def config_interrupt(app): # 进行所有拦截器的配置
    @app.before_request # 每次请求前处理
    def validate_params(): # 每次请求参数拦截
        if flask.request.url_rule: # 存在有URL路径规则
            rule = validations_properties.get(flask.request.url_rule.rule) # 获取规则
            if rule: # 有规则
                errors = validate_request_param(rule) # 验证
                if len(errors) > 0: # 此时有错误项
                    return render_template("common/error_500.html", errors=errors)

    @app.before_request
    def cookie_login(): # 负责Cookie免登录操作
        if not flask.session.get("uid"): # 现在没有发现session的指定属性
            uid = cookie_get("yootk-user") # 得到保存在浏览器中的Cookie信息
            if uid: # 现在可以发现用户id
                result_user = get_service_instance("UserSignService").get_user(uid)  # 获取业务层对象实例
                flask.session["uid"] = result_user.uid  # 保存用户id
                flask.session["photo"] = result_user.photo  # 用户的照片保存在数据库里面
                flask.session["admin"] = result_user.admin  # 管理员标记


    @app.before_request  # 每次请求前处理，进行session检测
    def session_check():
        # 前台的受限页面路径开头：/front/admin，主要是判断是否登录；
        # 后台首先页面的路径开头：/front/back，主要是判断是否拥有管理员标记（admin=1）
        if flask.request.path.startswith("/front/admin/"): # 前台管理页面
            if not flask.session.get("uid"): # 未登录
                message = "您还未登录，请先登录。"
                url = "/" # 跳转回到首页
                return render_template("common/forward.html", message=message, url=url)
        if flask.request.path.startswith("/back/admin/"): # 后台管理页面
            if not flask.session.get("uid"): # 未登录
                message = "您还未登录，请先登录。"
                url = "/" # 跳转回到首页
                return render_template("common/forward.html", message=message, url=url)
            else: # 登录过
                if flask.session.get("admin") != 1: # 不是管理员
                    message = "您不是管理员，无法进行访问！"
                    url = "/" # 跳转回首页
                    return flask.render_template("common/forward.html", message=message, url=url)

def config_errorhandle(app): # 错误页的配置
    @app.errorhandler(404)
    def http_status_404(exp): # 处理404错误
        print(traceback.format_exc())
        return render_template("common/error_404.html")
    @app.errorhandler(500)
    def http_status_500(exp):  # 处理404错误
        print(traceback.format_exc())
        return render_template("common/error_500.html")
    @app.errorhandler(Exception)
    def http_status_500_exception(exp):  # 处理404错误
        print(traceback.format_exc())
        return render_template("common/error_500.html")