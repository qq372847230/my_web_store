from app.extensions import database
from app.mapping.orm import User, Goods
from app.service.service_proxy import ServiceProxy # 导入事务代理的核心控制类
from app.util.proxy import ProxyFactory # 导入装饰器
@ProxyFactory(ServiceProxy)
class IndexService: # 负责用户注册与登录相关处理业务
    def list_search(self, current_page=1, line_size=20, keyword=None):
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
        return goods_list, goods_count[0]
    def list_item(self, iid, current_page=1, line_size=20):
        goods_list = database.session.query(Goods).filter(database.and_(Goods.dflag == 0, Goods.iid == iid)).order_by(
            Goods.gid.desc()).offset(
            (current_page - 1) * line_size).limit(line_size).all()  # 所有的商品
        goods_count = database.session.query(database.func.count(Goods.gid)).filter(database.and_(Goods.dflag == 0, Goods.iid == iid)).one()
        return goods_list, goods_count[0]
    def list(self, current_page=1, line_size=18):
        goods_list = database.session.query(Goods).filter(Goods.dflag == 0).order_by(Goods.gid.desc()).offset(
            (current_page - 1) * line_size).limit(line_size).all()  # 所有的商品
        return goods_list

@ProxyFactory(ServiceProxy)
class UserSignService: # 负责用户注册与登录相关处理业务
    def get_user(self, uid): # 根据uid获取用户信息
        return database.session.query(User).get(uid)
    def login(self, user):
        """
        用户登录检测的业务处理，该业务的流程为：
        1、通过uid查询用户的信息；
        2、通过获取到的用户信息进行密码的匹配；
        :param user:包含有用户名和密码的ORM对象
        :return:数据库对象信息
        """
        db_user = database.session.query(User).get(user.uid) # 根据id获取用户信息
        if db_user: # 有相关的uid数据存在
            if db_user.password == user.password: # 密码相同
                return db_user # 包含有用户的详细信息

    def add_user(self, user): # 实现用户增加业务的处理
        if database.session.query(User).get(user.uid): # 判断当前的用户是否存在
            return False # 如果存在直接返回False
        else: # 数据内容不存在
            user.admin = 0 # 新增的用户全部为普通用户
            user.name = "" # 避免None问题
            user.gender = "男" # 性别
            user.photo = "user-nophoto.png" # 默认的头像
            user.note = "" # 个人介绍
            database.session.add(user) # 实现数据的增加
            return True

@ProxyFactory(ServiceProxy)
class UserService: # 负责用户业务处理
    def edit_password(self, user, new_pwd): # 密码修改
        db_user = database.session.query(User).get(user.uid)
        if db_user: # 数据存在
            if db_user.password == user.password: # 匹配原始密码
                update_sql = "UPDATE user SET password=:password WHERE uid=:uid"
                result = database.session.execute(update_sql, {"password": new_pwd, "uid": user.uid})
                return result.rowcount > 0
        return False

    def edit_user(self, user): # 编辑用户信息
        update_sql = "UPDATE user SET name=:name, gender=:gender, birthday=:birthday, photo=:photo, note=:note WHERE uid=:uid"
        result = database.session.execute(update_sql, {"name": user.name, "gender": user.gender, "birthday": user.birthday,
                                                      "photo": user.photo, "note": user.note, "uid": user.uid})
        return result.rowcount > 0