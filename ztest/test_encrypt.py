from app.util.yootk_common import EncryptUtil# 导入所需要的加密模块
if __name__ == '__main__':
    password = "yootk-muyan-lixinghua"  # 原始密码
    print(EncryptUtil().get_encode_data(password))
    print(EncryptUtil().get_decode_data("VjJ4U1QyTXlVblJUV0hCV1ltdHdUbGxzVlRGTmJHeHpXak5vVDFZd2JEVlVNVkpEWVVkV1ZWSnFRbUZTYldoNldWVmtTMk5GTVZsVWJXaFlVakpvTTFkWE1IaGhNa2w1Vld4b1UxWkVRVGs9"))