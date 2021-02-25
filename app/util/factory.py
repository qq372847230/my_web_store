import importlib
SERVICE_MODEL_NAME = "app.service.front_service" # 模块名称
SERVICE_BACK_MODEL_NAME = "app.service.back_service" # 模块名称
def get_back_service_instance(class_name):
    service_object = getattr(importlib.import_module(SERVICE_BACK_MODEL_NAME), class_name)()
    return service_object  # 返回业务对象

def get_service_instance(class_name): # 设置要导入的类名称
    service_object = getattr(importlib.import_module(SERVICE_MODEL_NAME), class_name)()
    return service_object # 返回业务对象

