from app.util.proxy import InvocationHandler # 必须为此类的子类
from app.extensions import database # 导入数据库对象
import traceback
# 针对于有可能使用到事务的业务方法进行所有的前缀定义
TRANSACTION_METHOD_PREFIX = ("add", "edit", "delete", "update", "remove")
class ServiceProxy(InvocationHandler): # 定义有一个专属的代理业务类
    def __init__(self, target, function): # 设置代理的类以及操作方法
        super().__init__(target, function)
    def __call__(self, *args, **kwargs): # 实现真正的代理操作
        if self.check_method_name(self.function.__name__): # 检测当前的方法名称
            print("【ServiceProxy】｛BEGIN｝当前的业务操作需要开启事务（已经由SQLAlchemy自动开启了）。")
        try:
            result = self.function(*args, **kwargs) # 调用真实业务主题
            if self.check_method_name(self.function.__name__):
                print("【ServiceProxy】｛COMMIT｝进行事务提交，真正的更新数据库数据。")
                database.session.commit() # 事务提交
            return result # 返回真实业务主题的处理结果
        except Exception: # 如果产生异常则需要进行事务回滚
            print(traceback.format_exc())
            if self.check_method_name(self.function.__name__):
                print("【ServiceProxy】｛ROLLBACK｝当前的业务操作出现了问题，事务回滚处理。")
    def check_method_name(self, method_name):
        """
        检测当前要执行的业务方法名称前缀是否需要进行事务控制
        :param method_name: 方法名称
        :return: 如果需要事务控制，则返回True，否则返回False
        """
        for prefix in TRANSACTION_METHOD_PREFIX: # 迭代所有的前缀名称
            if method_name.startswith(prefix): # 有此前缀
                return True
        return False