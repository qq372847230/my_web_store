import sqlalchemy
from app.extensions import database # 导入数据库对象
class User(database.Model): # 创建一个映射类
    __tablename__ = "user" # 映射表名称
    uid = sqlalchemy.Column(sqlalchemy.String, primary_key=True) # 字段映射
    password = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    gender = sqlalchemy.Column(sqlalchemy.String)
    birthday = sqlalchemy.Column(sqlalchemy.Date)
    photo = sqlalchemy.Column(sqlalchemy.String)
    note = sqlalchemy.Column(sqlalchemy.String)
    admin = sqlalchemy.Column(sqlalchemy.Integer)
    def __repr__(self) -> str:
        return "uid = %s、password = %s" % (self.uid, self.password)

class Item(database.Model): # 创建一个映射类
    __tablename__ = "item" # 映射表名称
    iid = sqlalchemy.Column(sqlalchemy.BIGINT, primary_key=True) # 字段映射
    title = sqlalchemy.Column(sqlalchemy.String)

class Goods(database.Model): # 创建一个映射类
    __tablename__ = "goods" # 映射表名称
    gid = sqlalchemy.Column(sqlalchemy.BIGINT, primary_key=True) # 字段映射
    name = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Float)
    photo = sqlalchemy.Column(sqlalchemy.String)
    content = sqlalchemy.Column(sqlalchemy.String)
    dflag = sqlalchemy.Column(sqlalchemy.Integer)
    iid = sqlalchemy.Column(sqlalchemy.BIGINT)
    def __repr__(self) -> str:
        return "gid = %s、name = %s、price = %s、photo = %s、content = %s、dflag = %s" % (self.gid, self.name, self.price, self.photo, self.content, self.dflag)
