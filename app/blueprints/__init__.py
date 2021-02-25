from app.blueprints.index import index_bp
from app.blueprints.common import common_bp
from app.blueprints.front.user_sign import user_sign_bp
from app.blueprints.front.user_front import user_front_bp
from app.blueprints.back.goods_back import goods_back_bp
DEFAULT_BLURPINT = ( # 定义全部的蓝图以及访问路由
    (index_bp, "/"),  # 定义当前首页的访问蓝图配置
    (common_bp, "/"), # 定义公共的访问页面蓝图
    (user_sign_bp, "/"), # 定义用户登录与注册操作的蓝图
    (user_front_bp, "/front/admin/user"), # 定义个人中心的蓝图
    (goods_back_bp, "/back/admin/goods"), # 后台商品管理
)
def config_blueprint(app):
    """
    在Flask项目里面，所有的蓝图的配置一定要在程序启动的时候进行处理
    同时还需要向配置函数里面传入Flask的实例化对象
    :param app: Flask实例化对象
    :return: 不需要返回任何的内容，蓝图直接注册到app对象中即可
    """
    for blueprint, prefix in DEFAULT_BLURPINT:
        app.register_blueprint(blueprint, url_prefix=prefix) # 进行蓝图的注册