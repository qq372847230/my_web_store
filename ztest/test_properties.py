import os
from app.util.yootk_common import parse
MESSAGE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "app", "messages.properties")
def main():
    print("【os.path.realpath(__file__】%s" % os.path.realpath(__file__))
    print("【os.path.dirname(os.path.realpath(__file__)】%s" % os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    messages_properties = parse(MESSAGE_PATH)
    print("【获取属性】%s" % messages_properties.get("welcome.info"))
if __name__ == '__main__':
    main()