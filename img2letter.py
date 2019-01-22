# -*- coding: utf-8 -*-
from PIL import Image
import time

codeLib = '''@dB%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. '''  # 生成字符画所需的字符集
# codeLib = '''1234567890-=qwertyuiop[]\asdfghjkl;'zxcvbnm,./!@#$%^&*()_+|}{":?><QWERTYUIOPASDFGHJKLMNBVCXZ '''  # 生成字符画所需的字符集
count = len(codeLib)


def transform1(image_file):
    image_file = image_file.convert("L")  # 转换为黑白图片，参数"L"表示黑白模式
    codePic = ''
    for h in range(0, image_file.size[1]):  # size属性表示图片的分辨率，'0'为横向大小，'1'为纵向
        for w in range(0, image_file.size[0]):
            gray = image_file.getpixel((w, h))  # 返回指定位置的像素，如果所打开的图像是多层次的图片，那这个方法就返回一个元组
            codePic = codePic + codeLib[int(((count - 1) * gray) / 256)]  # 建立灰度与字符集的映射
        codePic = codePic + '\r\n'
    return codePic


def transform2(image_file):
    codePic = ''
    for h in range(0, image_file.size[1]):
        for w in range(0, image_file.size[0]):
            g, r, b = image_file.getpixel((w, h))
            gray = int(r * 0.299 + g * 0.587 + b * 0.114)
            codePic = codePic + codeLib[int(((count - 1) * gray) / 256)]
        codePic = codePic + '\r\n'
    return codePic

def save_txt(input_img,output_img):
    width=0.1
    height=0.1

    fp = open(input_img, 'rb')
    image_file = Image.open(fp)
    image_file = image_file.resize((int(image_file.size[0] * width*2 ), int(image_file.size[1] * height )))  # 调整图片大小

    img_txt=transform1(image_file)

    print('正在生成文字...')
    tmp = open(output_img, 'w')
    tmp.write(img_txt)
    tmp.close()
    print('文字已生成')

input_img='.\\input_img\\181206-132249.png'
output_img='.\\txt\\181206-132249.txt'
save_txt(input_img,output_img)
