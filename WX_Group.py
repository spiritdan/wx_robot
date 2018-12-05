import tuling
from wxpy import *

bot = Bot()
boring_group = bot.groups().search('123')[0]
##发送信息
boring_group.send('Hello,World！')
SourceSavePath = '.\\img\\'

@bot.register([boring_group, Group], TEXT)
def auto_reply(msg):
    if msg.is_at:
        # 回复消息内容和类型
        #answer = tuling.chat(msg.text)
        return msg,type(msg)

@bot.register([boring_group, Group],PICTURE)
def img_msg(msg):
    image_name = msg.file_name
    #friend = msg.chat
    print(msg.chat)
    print('接收图片'+image_name)
    msg.get_file(msg.file_name)
    print(msg.file_name)
    savepath=SourceSavePath+image_name
    # face(image_name)
    #print(savepath)
    msg.get_file(savepath)
    msg.reply_image(savepath)

    #msg.reply_image(msg.file_name)
embed()
