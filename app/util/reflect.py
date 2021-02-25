from copy import copy
from app.util.yootk_common import get_param_value # 导入参数的接收函数
import datetime # 需要进行字符串转为日期或日期时间的处理操作
import sqlalchemy.orm.attributes
import sqlalchemy.sql.sqltypes
def get_instance_object(clazz):
    """
    此函数将利用类反射的处理机制来实现指定ORM类的对象实例化操作，同时可以自动的与提交参数匹配实现属性的赋值
    :param clazz: 要进行反射操作的类名称（app.mapping.orm）
    :return: 已经赋值成功的ORM实例化对象
    """
    object = clazz() # 如果要想进行发射处理则首先要进行对象的实例化
    # 此时需要针对于已有的数据内容进行一次对象的拷贝，是为了防止成员内部的变化
    field_map = copy(object.__dict__) # 类之中的所有成员信息都自动保存在字典之中
    for key, value in field_map.items(): # 迭代全部的属性内容
        if key == '_sa_instance_state': # 找到实体类型，目的是找到映射字段
            orm_instance = value.class_ # 表示获取指定ORM实例化对象
            for column_key, column_value in orm_instance.__dict__.items():
                if not column_key.startswith("__"): # 不是“__”开头的信息
                    if type(column_value) == sqlalchemy.orm.attributes.InstrumentedAttribute: # 类属性结构
                        # setattr(要操作的对象实例，属性名称，属性内容)
                        setattr(object, column_key, get_parameter_value(column_key, column_value.type))
    return object
def get_parameter_value(param_name, param_type):
    """
    进行参数的接收，同时要根据参数的类型来进行参数的转型
    :param param_name: ORM属性名称（参数名称）
    :param param_type: 数据列的类型
    :return: 返回一个指定类型的参数转换后的结果
    """
    try:
        value = get_param_value(param_name) # 接收请求参数的内容
        if not value: # 没有此参数的内容
            return None # 返回一个空数据即可
        if type(param_type) == sqlalchemy.sql.sqltypes.String: # 字符串类型
            return value # 默认的类型就是字符串
        elif type(param_type) == sqlalchemy.sql.sqltypes.Integer: # 数字
            return int(value)
        elif type(param_type) == sqlalchemy.sql.sqltypes.BIGINT or type(param_type) == sqlalchemy.sql.sqltypes.BigInteger: # 数字
            return int(value)
        elif type(param_type) == sqlalchemy.sql.sqltypes.Float: # 浮点数
            return float(value)
        elif type(param_type) == sqlalchemy.sql.sqltypes.Date: # 日期类型
            return datetime.datetime.strptime(value, "%Y-%m-%d")
        elif type(param_type) == sqlalchemy.sql.sqltypes.DateTime: # 日期时间类型
            return datetime.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print(e)
        return None