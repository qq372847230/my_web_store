import base64 # 导入所需要的加密模块
if __name__ == '__main__':
    password = "yootk-muyan-lixinghua"  # 原始密码
    encode_pwd = base64.b64encode(password.encode("UTF-8")) # 二进制数据内容
    print(encode_pwd.decode("UTF-8"))
    print(base64.b64decode(encode_pwd).decode("UTF-8"))