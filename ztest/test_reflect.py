from app.util.reflect import get_instance_object
from app.mapping.orm import User
if __name__ == '__main__':
    get_instance_object(User) # 直接传递User类型