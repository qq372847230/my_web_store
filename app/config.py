# coding:UTF-8
import os  # 模块导入
from app.blueprints import config_blueprint
from app.extensions import config_errorhandle, config_extensions, config_interrupt, config_filter
from flask_wtf import CSRFProtect
BASE_DIR = os.path.abspath(os.path.dirname(__file__)) # 设置有一个基础路径
class Config(): # 【公共】WEB配置类
    @staticmethod
    def init_app(app): # 项目的初始化配置
        config_blueprint(app) # 进行蓝图的相关配置
        config_errorhandle(app) # 进行错误页的配置
        CSRFProtect(app) # 启用CSRF保护
        config_extensions(app) # 进行扩展包的启用配置
        config_interrupt(app) # 配置拦截器
        config_filter(app)
    SECRET_KEY = "www.my_web_store%s" % os.urandom(24)  # 定义加密配置
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024  # 上传限制
    UPLOADED_PHOTOS_DEST = os.path.join(BASE_DIR, 'static/upload')  # 上传文件保存目录
class DevelopmentConfig(Config): # 【某个环境】专属的配置类
    # 数据库链接的配置，此项必须，格式为（数据库+驱动://用户名:密码@数据库主机地址:端口/数据库名称）
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:mysqladmin@localhost/my_web_store"
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 对象跟踪
    SQLALCHEMY_ECHO = True  # 对象跟踪
config = { # 确定当前使用的系统环境配置
    "development" : DevelopmentConfig,
    # "test" : TestConfig,
    # "production" : ProductionConfig,
}