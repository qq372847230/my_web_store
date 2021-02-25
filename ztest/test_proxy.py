from app.util.proxy import ProxyFactory, InvocationHandler
@ProxyFactory(InvocationHandler)
class MessageService: # 核心业务
    def __init__(self, content):
        self.content = content
    def send(self): # 消息发送
        print("【MessageService】消息发送：%s" % self.content) # 模拟消息发送
        return "finish" # 发送完成后的信息提示
def main():
    service = MessageService("www.yootk.com")
    result = service.send() # 消息发送处理
    print("【客户端】消息发送的结果：%s" % result)
if __name__ == '__main__':
    main()