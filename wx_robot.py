import tuling
from wxpy import *
import img2letter,letter2img,combine_img,img2str_img
import os
import time
import HMM

bot = Bot()
my_friend = bot.friends().search('领悟', sex=MALE, city='苏州')[0]

my_friend.send('Hello, WeChat!')

@bot.register([my_friend, User],TEXT)
def reply(msg):
        print(msg.sender,type(msg.sender))
        if msg.sender==my_friend:
            # 回复消息内容和类型
            return '没空'

embed()


msg=input()