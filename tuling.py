import requests, json, random, time
from sys import exit
'''
复现第0个关卡当中的人工智能案例，包括实现对话。
提示：
1，实现对话，你可以调用图灵机器人来完成：http://www.tuling123.com/ 
2，帮助文档：https://www.kancloud.cn/turing/web_api/522992 
3，传输数据需要json格式，你可以利用 json.dumps() 来生成json格式的内容。此处的括号内，填写的是字典。

'''
#text = input('图灵：咱开始聊天吧\n你：')
#time.sleep(1)
url = 'http://openapi.tuling123.com/openapi/api/v2'
# 注册太麻烦，就用案例里的id和key了
userid = str(random.randint(1, 1000000000000000000000))
apikey = '16ed0d5c470c42f9b96600e6b6d499f7'


# 超过1w有风险，19-01-19
def add_q(text):
    data = json.dumps({
        "reqType": 0,
        "perception": {
            "inputText": {
                "text": text
            },
        },
        "userInfo": {
            "apiKey": apikey,
            "userId": userid
        }
    })
    return data


def chat(text):
    data = add_q(text)
    req = requests.post(url, data)
    answer = json.loads(req.text)['results'][0]['values']['text']
    return answer