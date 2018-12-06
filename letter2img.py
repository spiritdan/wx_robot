# coding: utf-8
from io import StringIO
import os
from PIL import Image, ImageFont, ImageDraw
import pygame
def convert(filename,text,index,tmp_path):
    pygame.init()
    #text = "this is a test,test 123\nfdsfadfadfafadfa\nljfdskljflsdakjfldaskjflskdjflk\ntrtrrewrtert"
    im = Image.new("RGB", (300, 50), (255, 255, 255))
    #dr = ImageDraw.Draw(im)
    #font = ImageFont.truetype(os.path.join("fonts", "sinsun.ttc"), 18)
    fontpath = "C:\\Windows\\Fonts"
    font = pygame.font.Font(os.path.join(fontpath, "simsun.ttc"), 14) #dr.text((10, 5), text, font=font, fill="#000000")
    rtext = font.render(text, True, (0, 0, 0), (255, 255, 255))
    index='{:0>4}'.format(index)
    if not os.path.exists(tmp_path+"{0}\\".format(filename,index)):
        os.makedirs(tmp_path+"{0}\\".format(filename,index))
    #print(tmp_path + "{0}\\{0}{1}.png".format(filename,index))
    pygame.image.save(rtext,tmp_path + "{0}\\{0}{1}.png".format(filename,index))

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