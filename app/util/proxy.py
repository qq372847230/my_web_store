import types # 类型模块
class ProxyFactory: # 定义装饰器
    def __init__(self, invocation_handle_clazz):
        if issubclass(invocation_handle_clazz, InvocationHandler) or \
                invocation_handle_clazz is InvocationHandler: # 确定了代理类型
            self.handle = invocation_handle_clazz # 保存代理类
        else:
            raise InvocationHandlerException(invocation_handle_clazz) # 抛出异常
    def __call__(self, *args, **kwargs):
        return Proxy(args[0], self.handle)
class Proxy: # 完成核心代理
    """
        执行核心的代理调用，可以执行到此代码的部分一定是InvocationHandler子类
    """
    def __init__(self, target_clazz, invocation_handle_clazz):
        """
        进行代理类对象实例化
        :param target_clazz: 真实业务主题的对象类型
        :param invocation_handle_clazz: 要使用到的代理主题的类型
        """
        self.target_clazz = target_clazz
        self.invocation_handle_clazz = invocation_handle_clazz
        self.handlers = dict() # 保存所有的执行处理类，避免重复实例化
    def __call__(self, *args, **kwargs): #
        self.object = self.target_clazz(*args, **kwargs) # 获取一个真实业务主题对象
        return self # 返回当前对象
    def __getattr__(self, item):
        exists = hasattr(self.object, item) # 在指定的类中是否存在有特定结构
        result = None # 真实业务的处理结果
        if exists: # 存在有特定的结构
            result = getattr(self.object, item) # 获得操作类型
            if isinstance(result, types.MethodType): # 调用的是一个方法
                if self.handlers.get(result) is None: # 没有此类型的对象
                    self.handlers[result] = self.invocation_handle_clazz(self.object, result) # 实例化业务对象
                return self.handlers[result] # 返回操作对象
            else: # 调用的是类属性
                return result
        return result
class InvocationHandler: # 定义代理的执行标准
    def __init__(self, target, function): # 执行标准初始化
        self.target = target
        self.function = function
    def __call__(self, *args, **kwargs):
        print("【公共代理功能】", self.target, self.function, args, kwargs)
        return self.function(*args, **kwargs) # 调用真实业务主题
class InvocationHandlerException(Exception):
    """
    自定义异常，只要使用的类没有继承InvocationHandler父类则抛出
    """
    def __init__(self, clazz):
        super(InvocationHandlerException, self).__init__(
            clazz, "，不是一个代理处理类。")