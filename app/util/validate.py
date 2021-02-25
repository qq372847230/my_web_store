from app.util.yootk_common import get_param_value # 接收参数函数
import app.extensions  # 读取消息资源
import flask # 要通过session获取验证码
import re # 所有的数据结构验证最佳的做法是使用正则表达式
def validate_request_param(rule): # 进行指定规则验证
    """
    对于所有的请求参数进行规则验证
    :param rule: 规则的定义（参数名称:规则|参数名称:规则|...）
    :return: 返回验证错误的内容
    """
    # 字典key = 参数名称、value = 错误的内容
    errors = dict() # 所有的错误信息保存在字典中
    validate_rules = rule.split("|") # 根据“|”拆分规则
    for rule in validate_rules: # 进行规则的配置
        param_info = rule.split(":") # 第一个数据为参数名称，第二个数据为规则
        param_value = get_param_value(param_info[0]) # 根据参数名称接收内容
        if param_info[1].lower() == "string": # 字符串内容，不能为空
            if not validate_string_data(param_value): # 没有字符串数据
                errors[param_info[0]] = app.extensions.messages_properties.get("string.error.msg") # 错误信息
        elif param_info[1].lower() == "int": # 整数规则
            if not validate_int_data(param_value): # 验证数字
                errors[param_info[0]] = app.extensions.messages_properties.get("int.error.msg") # 错误信息
        elif param_info[1].lower() == "float": # 浮点数规则
            if not validate_float_data(param_value): # 验证数字
                errors[param_info[0]] = app.extensions.messages_properties.get("float.error.msg") # 错误信息
        elif param_info[1].lower() == "date": # 日期规则
            if not validate_date_data(param_value): # 验证数字
                errors[param_info[0]] = app.extensions.messages_properties.get("date.error.msg") # 错误信息
        elif param_info[1].lower() == "datetime": # 日期规则
            if not validate_datetime_data(param_value): # 验证数字
                errors[param_info[0]] = app.extensions.messages_properties.get("datetime.error.msg") # 错误信息
        elif param_info[1].lower() == "rand": # 日期规则
            if not validate_rand_data(param_value): # 验证数字
                errors[param_info[0]] = app.extensions.messages_properties.get("rand.error.msg") # 错误信息
        elif param_info[1].lower() == "boolean": # 日期规则
            if not validate_boolean_data(param_value): # 验证数字
                errors[param_info[0]] = app.extensions.messages_properties.get("boolean.error.msg") # 错误信息
    return errors # 返回错误信息
def validate_string_data(value): # 进行字符串是否为空的判断
    if value: # 内容不为空
        return True # 返回True
    return False # 验证失败，表示有错误
def validate_int_data(value): # 验证是否为整数
    if validate_string_data(value): # 数据不为空再验证
        pattern = r"^\d+$" # 正则规则
        return re.match(pattern, value) # 正则验证数据
    return False  # 验证失败
def validate_float_data(value): # 验证是否为浮点数
    if validate_string_data(value): # 数据不为空再验证
        pattern = r"^\d+(\.\d+)?$" # 正则规则
        return re.match(pattern, value) # 正则验证数据
    return False  # 验证失败
def validate_date_data(value): # 验证是否为日期
    if validate_string_data(value): # 数据不为空再验证
        pattern = r"^\d{4}-\d{2}-\d{2}$" # 正则规则
        return re.match(pattern, value) # 正则验证数据
    return False  # 验证失败
def validate_datetime_data(value): # 验证是否为日期时间
    if validate_string_data(value): # 数据不为空再验证
        pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$" # 正则规则
        return re.match(pattern, value) # 正则验证数据
    return False  # 验证失败
def validate_rand_data(value): # 验证是否为正确的验证码
    if validate_string_data(value): # 数据不为空再验证
        rand = flask.session.get("imgrand") # 获取生成验证码
        if rand: # 现在有验证码
            return rand.upper() == value.upper() # 验证码检测
    return False  # 验证失败
def validate_boolean_data(value): # 验证是否为布尔型
    if validate_string_data(value): # 数据不为空再验证
        return value.upper == "TRUE" or value.upper == "FALSE" # 为真
    return False  # 验证失败