import flask
import hashlib
import base64
import uuid, os
def get_md5_code(value): # 进行MD5加密操作
    return hashlib.md5(value.encode("UTF-8")).hexdigest()
def get_param_value(param_name): # 获取参数，该参数可能通过表单获取也可能通过地址获取
    value = flask.request.args.get(param_name) # 获取路径重写参数
    if not value: # 没有接收到value数据
        value = flask.request.form.get(param_name) # 根据表单获取
    return value

def get_split_param(): # 接收所有的分页参数
    cp = get_param_value("cp") # cp为current_page变量（业务方法的参数名称）的简写
    ls = get_param_value("ls") # ls为line_size变量（业务方法的参数名称）的简写
    kw = get_param_value("kw") # kw为keyword变量（业务方法的参数名称）简写
    if not cp: # 没有传递cp参数
        cp = 1 # 默认从首页开始
    else: # 有传递的参数
        cp = int(cp) # 数据转型
    if not ls : # 没有传递ls参数
        ls = 5 # 默认的加载数据行数
    else:
        ls = int(ls) # 数据转型
    if not kw: # 没有kw参数内容
        kw = ""
    return cp, ls, kw


class Properties: # 定义属性读取
    def __init__(self, file_name): # 进行属性操作初始化
        self.file_name = file_name # 保存要读取的资源文件
        self.properties = {} # 读取到的数据信息保存在字典之中
        try:
            fopen = open(self.file_name, "r") # 打开资源文件
            for line in fopen: # 读取每一行数据
                line = line.strip() # 去掉空格
                # 如果发现要读取的数据行包含有“=”并且不是以“#”开头
                if line.find("=") > 0 and not line.startswith("#"):
                    msg = line.split("=") # 根据等号进行拆分
                    self.properties[msg[0].strip()] = msg[1].strip() # 保存属性
        except Exception as e:
            raise e # 向上抛出异常对象
        else:
            fopen.close() # 关闭文件对象
    def has_key(self, key): # 是否存在有指定的key
        return key in self.properties
    def get(self, key, default_value = ""): # 根据key查找数据
        if key in self.properties:
            return self.properties[key] # 返回对应的字典项
        return default_value # 没有内容返回默认数据内容

def parse(file_name): # 属性工厂函数
    return Properties(file_name)

def cookie_clear(response): # 清空Cookie数据
    for cookie in flask.request.cookies: # 获取全部的Cookie
        response.delete_cookie(key=cookie) # 直接删除Cookie

def cookie_set(response, key, value, max_age=86400):
    """
    进行Cookie数据的设置，默认的失效时间为10天
    :param response: HTTP回应对象
    :param key: HTTP回应的数据key
    :param value: Cookie内容
    :param max_age:默认的存储时间
    :return: None
    """
    response.set_cookie(key=key, value=EncryptUtil().get_encode_data(value), max_age=max_age, path="/")
def cookie_get(key):
    """
    根据key获取指定名称的Cookie数据
    :param key: 保存数据时设置的key信息
    :return: 对应的Cookie内容，如果没有指定的key返回None
    """
    value = flask.request.cookies.get(key) # 通过请求头信息获取Cookie数据
    if value: # 有对应的value数据存在
        return EncryptUtil().get_decode_data(value) # 直接返回数据

class EncryptUtil: # 加密工具类
    def __init__(self):
        self.salt = "yootk.com" # 盐值可以随意设置
        self.repeat = 5 # 重复加密的次数
    def get_encode_data(self, str): # 获取加密后的数据
        encode_data = "{%s}%s" % (self.salt, str) # 加盐值后的原始数据
        for num in range(self.repeat): # 多次循环
            encode_data = base64.b64encode(encode_data.encode("UTF-8")).decode("UTF-8")
        return encode_data
    def get_decode_data(self, str): # 解密
        decode_data = str
        for num in range(self.repeat):
            decode_data = base64.b64decode(decode_data.encode("UTF-8")).decode("UTF-8")
        return decode_data.replace("{%s}" % self.salt, "")

def upload_file(storage, filename=None, default_filename="nophoto.png"): # 文件上传
    if storage: # 有文件上传
        if not storage.mimetype == "application/octet-stream": # 有文件上传
            if filename == None or filename == default_filename: # 文件没有命名
                filename = str(uuid.uuid1()) + "." + storage.mimetype[storage.mimetype.rindex("/") + 1 : ] # 新的文件名称
                save_dir = flask.current_app.config["UPLOADED_PHOTOS_DEST"] # 默认配置的上传目录
                storage.save(os.path.join(save_dir, filename))
                return filename # 返回图片名称
            else: # 有图像上传
                save_dir = flask.current_app.config["UPLOADED_PHOTOS_DEST"]  # 默认配置的上传目录
                storage.save(os.path.join(save_dir, filename))
                return filename
        else:
            return filename
        return filename # 返回原始的图片名称