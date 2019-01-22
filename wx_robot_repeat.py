import tuling
from wxpy import *
import img2letter,letter2img,combine_img,img2str_img
import os
import time
import HMM

bot = Bot()
my_friend = bot.friends().search('spirit')[0]

my_friend.send('快对我说：“你先回答那个问题下面那个问题先')

@bot.register([my_friend, User],TEXT)
def reply(msg):
        print(msg.sender,my_friend,type(msg.sender))
        msg2 = msg.text.replace('下面那个问题', '下面那个问题再下面那个问题', 1)
        #print(msg2)
        if msg.sender == my_friend:
            print('test')
            # 回复消息内容和类型
            return msg2

'''
@bot.register([my_friend, User],TEXT)
def auto_reply(msg):
    if msg.sender == my_friend:
        start = msg.text
        print(start)
        song = HMM.generate(start)
        print('正在写歌')
        print(type(song))
        print(song)
        # 回复消息内容和类型tuling
        #answer = tuling.chat(msg.text)
        #return answer
        return song
'''
embed()


