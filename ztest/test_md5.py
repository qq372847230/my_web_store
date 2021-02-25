from hashlib import md5 # md5是提供的一种加密算法函数
if __name__ == '__main__':
    password = "0104180547"  # 原始密码
    code = md5(password.encode("UTF-8")).hexdigest()
    print(code)
    print(len(code)) # 计算长度