from flask import Blueprint # 导入蓝图配置
from flask import render_template # 导入模版跳转函数
from app.util.factory import get_service_instance
from app.util.reflect import get_instance_object # 反射进行对象实例化处理
from app.util.yootk_common import upload_file, get_param_value, get_split_param
index_bp = Blueprint(name="index", import_name=__name__)
@index_bp.route("/") # 定义首页路由
def index():
    goods_list = get_service_instance("IndexService").list()
    return render_template("index.html", goodses=goods_list)
@index_bp.route("/item.index/<int:iid>") # 定义首页路由
def item_index(iid):
    cp, ls, kw = get_split_param()  # 接收分页控制参数
    goods_list, goods_count = get_service_instance("IndexService").list_item(iid, cp)
    return render_template("index_search.html", goodses=goods_list, current_page=cp, url="/item.index/%s" % iid, all_recorders=goods_count)
@index_bp.route("/search.index") # 定义首页路由
def search_index():
    cp, ls, kw = get_split_param()  # 接收分页控制参数
    goods_list, goods_count = get_service_instance("IndexService").list_search(current_page=cp, keyword=kw)
    return render_template("index_search.html", goodses=goods_list, current_page=cp, url="/search.index", all_recorders=goods_count, keyword=kw)