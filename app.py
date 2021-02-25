import app # 导入app模块，自动获取初始化操作
flask_app = app.create_app("development") # 获取指定的运行环境的Flask对象
if __name__ == '__main__':
    flask_app.run(port=80, debug=True) # 运行WEB程序