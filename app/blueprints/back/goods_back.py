from flask import Blueprint, session, render_template, request, make_response
from app.mapping.orm import Goods
from app.util.factory import get_back_service_instance
from app.util.reflect import get_instance_object # 反射进行对象实例化处理
from app.util.yootk_common import upload_file, get_param_value, get_split_param
goods_back_bp = Blueprint(name="goods_back", import_name=__name__) # 前台用户蓝图


@goods_back_bp.route("/list.action", methods=["GET", "POST"])
def list_handle():  # 修改密码页面
    cp, ls, kw = get_split_param()  # 接收分页控制参数
    items, goods_list, goods_count = get_back_service_instance("GoodsService").split_list_goods(cp, ls, kw)
    return render_template("/back/admin/goods/goods_list.html",
                           items=item_converter_dict(items), current_page=cp, keyword=kw,
                           goodses=goods_list, all_recorders=goods_count)

@goods_back_bp.route("/add.page")
def goods_add_page():
    items = get_back_service_instance("GoodsService").pre_add() # 业务调用
    return render_template("/back/admin/goods/goods_add.html", items=items)
@goods_back_bp.route("/add.action", methods=["POST"])
def goods_add_handle():
    goods = get_instance_object(Goods) # 获取商品表单数据
    goods.photo = upload_file(request.files.get("file"), filename=goods.photo, default_filename="nophoto.png")
    message = "商品信息添加失败，请重新进行商品信息输入！"
    url = "/back/admin/goods/add.page"
    if get_back_service_instance("GoodsService").add_goods(goods): # 增加成功
        message = "商品信息添加成功！"
    return render_template("common/forward.html", message=message, url=url)
@goods_back_bp.route("/edit.page")
def goods_edit_page():
    gid = int(get_param_value("gid")) # 得到修改商品编号
    items, goods = get_back_service_instance("GoodsService").pre_edit(gid)
    if goods: # 可以查询到数据内容
        return render_template("/back/admin/goods/goods_edit.html", items=items, goods=goods)
    else: # 没有数据
        message = "没有此商品信息，请确认后再进行编辑！"
        url = "/back/admin/goods/list.action"
        return render_template("common/forward.html", message=message, url=url)
@goods_back_bp.route("/edit.action", methods=["POST"])
def goods_edit_handle():
    goods = get_instance_object(Goods)  # 获取商品表单数据
    goods.photo = upload_file(request.files.get("file"), filename=goods.photo, default_filename="nophoto.png")
    message = "商品信息修改失败，请重新确认该商品内容是否存在！"
    url = "/back/admin/goods/list.action"
    if get_back_service_instance("GoodsService").edit_goods(goods):  # 增加成功
        message = "商品信息修改成功！"
    return render_template("common/forward.html", message=message, url=url)
@goods_back_bp.route("/delete.action")
def goods_delete_handle():
    gid = int(get_param_value("gid"))  # 得到删除商品编号
    message = "商品信息删除失败，请重新确认该商品内容是否存在！"
    url = "/back/admin/goods/list.action"
    if get_back_service_instance("GoodsService").delete_goods(gid):  # 增加成功
        message = "商品信息删除成功！"
    return render_template("common/forward.html", message=message, url=url)
def item_converter_dict(item_list): # 需要将列表转为字典
    item_dict = dict() # 定义字典
    for item in item_list: # 进行转换
        item_dict[item.iid] = item.title
    return item_dict