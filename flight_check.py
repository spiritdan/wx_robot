import requests,json
#引用requests和bs4（BeautifulSoup4的缩写）,如果没有安装bs4，可以使用pip install beautifulsoup4下载。
from urllib.request import quote
#quote函数，可以帮我们把内容转为标准的url格式，作为网址的一部分打开。
def check_flight():
    #将汉字，用gbk格式编码，赋值给gbkmovie。
    urlflight = 'http://webapp.veryzhun.com/h5/flightsearch?fnum=ZH9516&date=2018-12-04&token=74e5d4cac3179fc076af4f401fd4ebe3'
    #将gbk格式的内容，转为url，然后和前半部分的网址拼接起来。
    res =requests.get(urlflight)
    #print(res)
    #下载水形物语的搜索页面
    js_flight=json.loads(res.text)[0]
    #解析网页。
    print('实际到达时间：{}'.format(js_flight['FlightArrtimeDate']))
    print('预计到达时间：{}'.format(js_flight['FlightArrtimeReadyDate']))
    return js_flight['FlightArrtimeDate'],js_flight['FlightArrtimeReadyDate']