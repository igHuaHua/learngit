import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter

char = 'qwertyuiopasdfghjklzxcvbnm'

def charColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def rndColor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

def char2list():
    return random.choice(char)

def drawchar():
    im = Image.new('RGB',(300,60),'white')
    idcode = ImageDraw.ImageDraw(im)
    myfont = ImageFont.truetype(r'C:\windows\fonts\Arial.ttf', size=50)
    width,height = im.size
    for x in range(width):
        for y in range(height):
            idcode.point((x, y), fill=rndColor())

    for i in range(4):
        idcode.text((60*i,0),char2list(),font=myfont,fill=charColor())
    im2 = im.filter(ImageFilter.BLUR)
    im2.show()

h = char2list()
d = drawchar()