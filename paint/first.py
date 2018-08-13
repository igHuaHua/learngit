from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    #设置字体型号，大小
    myfont = ImageFont.truetype(r'C:\windows\fonts\Arial.ttf', size=40)
    #设置字体颜色，可用颜色名称表示，也可用代码
    fillcolor = 'black'
    #获取图片的宽，高
    width, height = img.size
    #设置字体起始位置，因为这里一个字体占20宽，两个就40。绑定字体型号，颜色
    draw.text((width-60, 0), '99+', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')
    img.show()

    return 0
if __name__ == '__main__':
    image = Image.open('C:\\Users\\28240\PycharmProjects\\paint\\01.jpg')
    add_num(image)


#参考资料：https://blog.csdn.net/zhangziju/article/details/79123275#t9