import os
import jieba
#IMAGES_PATH='.\\tmp\\181206-143020'
#for name in os.listdir(IMAGES_PATH):
#    print(name)

#数据格式化，保留4位，用0补足显示0019
#print('{:0>4}'.format('19'))

import jieba
s = '菊花@spirit'
print(s.find('@'))
cut = list(jieba.cut(s, cut_all=True))
print(cut)
'''
file = open('Text/jielun.txt','r')
corpus = file.read()
walden = list(jieba.cut(corpus))
#walden = walden.split()
print(walden)
'''
