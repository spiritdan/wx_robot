import tuling
from wxpy import *
import img2letter,letter2img,combine_img,img2str_img
import os
import time
import HMM
import nltk
bot = Bot()
print(bot.groups().search())
group_name = bot.groups().search('Python小课-山顶群(4)')[0]
##发送信息
group_name.send('@我 +一个关键词 来替杰伦写歌了。直接发送图片转字符画')
SourceSavePath = '.\\input_img\\'

@bot.register([group_name, Group], TEXT)
def auto_reply(msg):
    if msg.is_at:
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

@bot.register([group_name, Group],PICTURE)
def img_msg(msg):
    image_name = msg.file_name.split(".")[0]
    #friend = msg.chat
    print(msg.chat)
    print('接收图片'+image_name)
    #msg.get_file(msg.file_name)

    print(msg.file_name)
    savepath=SourceSavePath+msg.file_name
    print("savepath:"+savepath)
    msg.get_file(savepath)

    extension = '.png'
    input_img_path = SourceSavePath
    print("开始转换")
    #input_img='.\\input_img\\181206-132249.png'
    #output_img='.\\txt\\181206-132249.txt'
    #img2letter.save_txt(savepath,output_img)
    reply_img=img2str_img.convert_img(image_name,input_img_path, extension)
    print("reply_img:"+reply_img)
    print("转换结束")
    print("savepath"+savepath)
    print('reply_img'+reply_img)
    if os.path.exists(reply_img):
        print("reply_img已生成")
        time.sleep(0.5)
    else:
        print("reply_img还没完成")
    #msg.reply_image(savepath)
    #回复图片必须png格式
    msg.reply_image(reply_img)

embed()
