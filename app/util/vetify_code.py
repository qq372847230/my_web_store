# coding:UTF-8
import random # 使用随机数
from PIL import Image, ImageDraw, ImageFont, ImageFilter # pip install Pillow
def vetifycode():
    total = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345789" # 备选内容
    width = 130 # 图片宽度
    height = 36 # 图片高度
    bgColor = random_color()
    image = Image.new("RGB", (width, height), bgColor) # 生成一个新图片对象
    font = ImageFont.truetype("app/static/fonts/consola.ttf", 35)# 设置字体
    draw = ImageDraw.Draw(image)  # 创建draw对象
    str = "" # 保存生成的验证码字符串
    for item in range(5):    # 输出每一个文字
        text = random.choice(total) # 随机挑取数据
        str += text # 保存生成文本
        draw.text((2 + random.randint(4, 7) + 20 * item, 2 + random.randint(3, 7)), text=text, fill=random_color(is_light=False), font=font)
    for num in range(8): # 干扰线
        x1 = random.randint(0, width / 2)
        y1 = random.randint(0, height / 2)
        x2 = random.randint(0, width)
        y2 = random.randint(height / 2, height)
        draw.line(((x1, y1), (x2, y2)), fill="white", width=1)
    image = image.filter(ImageFilter.FIND_EDGES) # 数据模糊处理
    return image, str
def random_color(is_light = True):
    return (random.randint(0 ,127) + int(is_light) * 128,random.randint(0,127) + int(is_light) * 128,random.randint(0,127) + int(is_light) * 128)