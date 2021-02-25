import io
import flask
from app.util.yootk_common import get_param_value
from flask import make_response
from flask import Blueprint
from app.util.vetify_code import vetifycode
common_bp = Blueprint(name="common", import_name=__name__)
@common_bp.route("/vetify.check", methods=["GET", "POST"])
def check_code():
    result = "False" # 默认的返回结果
    code = get_param_value("code") # 获取验证码
    rand = flask.session["imgrand"] # 获取session中的验证码
    if code and rand: # 两个内容都不为空
        result = str (rand.upper() == code.upper()) # 不区分大小写比较
    response = flask.make_response(result) # 如果有其他问题还需要设置头信息
    return response
@common_bp.route("/vetify.code")
def vetify_code(): # 生成验证码
    image, str = vetifycode() # 获取生成的验证码图片和生成的内容
    buf = io.BytesIO() # 通过内存流保存生成的验证码图片
    image.save(buf, "png") # 设置图片的类型
    buf_str = buf.getvalue()
    response = make_response(buf_str) # 创建响应对象
    response.headers["Content-Type"] = "image/png" # 设置响应的MIME类型
    flask.session["imgrand"] = str  # 保存生成的验证码
    return response # 获取响应