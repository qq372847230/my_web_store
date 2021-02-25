from app.extensions import database
from app.mapping.orm import Goods, Item
from app.service.service_proxy import ServiceProxy  # 导入事务代理的核心控制类
from app.util.proxy import ProxyFactory  # 导入装饰器


@ProxyFactory(ServiceProxy)
class GoodsService:  # 负责用户注册与登录相关处理业务
    def delete_goods(self, gid):  # 逻辑删除
        update_sql = "UPDATE goods SET dflag=1 WHERE gid=:gid"
        result = database.session.execute(update_sql, {"gid": gid})
        return result.rowcount > 0

    def pre_edit(self, gid):  # 修改前的查询
        goods_obj = database.session.query(Goods).filter(database.and_(Goods.dflag == 0, Goods.gid == gid)).all()[0]
        items = database.session.query(Item).all()
        return items, goods_obj

    def edit_goods(self, goods):
        update_sql = "UPDATE goods SET name=:name, price=:price, photo=:photo, content=:content, iid=:iid WHERE gid=:gid AND dflag=0"
        result = database.session.execute(update_sql, {"name": goods.name, "price": goods.price, "photo": goods.photo,
                                                       "content": goods.content, "iid": goods.iid, "gid": goods.gid})
        return result.rowcount > 0

    def pre_add(self):  # 增加前的准备
        return database.session.query(Item).all()

    def add_goods(self, goods):
        goods.dflag = 0  # 逻辑删除标记
        database.session.add(goods)  # 商品增加
        return True

    def list_goods(self):  # 商品列出
        goods_list = database.session.query(Goods).filter(Goods.dflag == 0).all()  # 所有的商品
        items = database.session.query(Item)  # 查询所有的分类
        return items, goods_list

    def split_list_goods(self, current_page=1, line_size=5, keyword=None):  # 商品列出
        if keyword:  # 有模糊查询关键字
            goods_list = database.session.query(Goods).filter(
                database.and_(Goods.dflag == 0, Goods.name.like("%" + keyword + "%"))).order_by(
                Goods.gid.desc()).offset(
                (current_page - 1) * line_size).limit(line_size).all()  # 所有的商品
            goods_count = database.session.query(database.func.count(Goods.gid)).filter(
                database.and_(Goods.dflag == 0, Goods.name.like("%" + keyword + "%"))).one()
        else:  # 没有查询关键字
            goods_list = database.session.query(Goods).filter(Goods.dflag == 0).order_by(Goods.gid.desc()).offset(
                (current_page - 1) * line_size).limit(line_size).all()  # 所有的商品
            goods_count = database.session.query(database.func.count(Goods.gid)).filter(Goods.dflag == 0).one()
        items = database.session.query(Item)  # 查询所有的分类
        return items, goods_list, goods_count[0]
