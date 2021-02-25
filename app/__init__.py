from flask import Flask # 导入Flask程序类
from app.config import config # 导入环境配置类

def create_app(config_name):
    """
    通过此函数实现Flask对象的创建，在进行对象创建的同时还需要去考虑其他组件的初始化的处理问题
    本次的初始化操作组件包括：
        1、一些程序的扩展支持；
        2、蓝图的加载；
        3、错误页的配置；
        4、拦截器（钩子函数）的配置；
        5、自定义过滤器的使用；
        6、CSRF校验保护。
    :param config_name: 定义不同的启动模式，项目开发会分为“开发模式”、“测试模式”、“生产模式”
    :return: 可以直接使用的Flask对象
    """
    app = Flask(__name__) # 创建有一个Flask的对象
    # 根据传入的配置的名称来加载相应的配置，如果此名称没有传输则使用默认的开发环境配置
    app.config.from_object(config.get(config_name) or "development")
    # 如果现在有其他的需要也可以执行一些额外的初始化的操作
    config.get(config_name).init_app(app)
    return app