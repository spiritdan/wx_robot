import tuling
from wxpy import *
import flight_check
import time

bot = Bot()
ftime = flight_check.check_flight()
plan_time = ftime[1][-8:-3]
#print(ftime[1])

#print(now)

while True:
    now = time.localtime(time.time())
    now_str = str(now.tm_hour) + ':' + str(now.tm_min)
    #now_str="11:1"
    now_str=now_str.replace(":",'')
    real_time=flight_check.check_flight()[0][-7:-3]
    #real_time = "23:17"
    real_time=real_time.replace(':','')

    print(real_time,now_str)
    if real_time!="" and int(real_time)<=int(now_str):
        print("时间到！")
        break
    print(now_str)
    time.sleep(30)

real_time=flight_check.check_flight()[0]
print(real_time)
my_friend = bot.friends().search('爱戴', sex=FEMALE, city='南通')[0]
my_friend.send('航班ZH9516已到达，降落时间{0}，请通知接驾~~'.format(real_time))
@bot.register([my_friend, User],TEXT)
def reply(msg):
        print(msg.sender,type(msg.sender))
        answer = tuling.chat(msg.text)
        return answer

embed()


