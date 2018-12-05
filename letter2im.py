# coding: utf-8
from io import StringIO
import os
from PIL import Image, ImageFont, ImageDraw
import pygame
def convert(text,index):
    pygame.init()
    #text = "this is a test,test 123\nfdsfadfadfafadfa\nljfdskljflsdakjfldaskjflskdjflk\ntrtrrewrtert"
    im = Image.new("RGB", (300, 50), (255, 255, 255))
    #dr = ImageDraw.Draw(im)
    #font = ImageFont.truetype(os.path.join("fonts", "sinsun.ttc"), 18)
    fontpath = "C:\\Windows\\Fonts"
    font = pygame.font.Font(os.path.join(fontpath, "simsun.ttc"), 14) #dr.text((10, 5), text, font=font, fill="#000000")
    rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))
    pygame.image.save(rtext, "c:\\tmp\\t{0}.png".format(index))

file=open("c:\\tmp\\output.txt")
j=0
for i in file.readlines():
    convert(i,j)
    j=j+1
#SIO编码的问题
#sio = StringIO()
#print(type(rtext))
#sio=BytesIO()
#print(rtext)
#pygame.image.save(rtext, sio)
#sio.seek(0)
#line = Image.open(sio)
#im.paste(line, (10, 5))
#im.show()
#im.save("c:\\tmp\\t.png")