import re
import requests
from time import strftime
import time, datetime

# URL地址
schoolWebURL1 = 'http://10.10.42.3'
schoolWebURL2 = 'http://10.10.43.3'

while (True):
    response = requests.get(schoolWebURL1)

    # 正则表达式，匹配<title>标签中的内容
    pattern = re.compile('<title>(.*?)</title>', re.S)
    title = re.findall(pattern, response.text)
    title = title[0]  # 将格式转为字符串

    if title == '注销页':
        now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(now_date, "\n*******", '连接正常 :)')
        print("*******", "状态码{}".format(response))  # 打印状态码
        # print("*******", "正在等待下一次检测...\n")
        input("******* 请按下回车来执行新的检测...\n")
        pass

    else:
        user = 'XXXXXXXXXX'  # 学号
        p = 'XXXXXXXXXX'  # 密码
        t = str(int(round(time.time() * 1000)))  # 毫秒级时间戳
        schoolWebLoginURL = schoolWebURL1 + '/drcom/login?callback=dr' + t + '&DDDDD=' + user + '&upass=' + p + '&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&_=' + t
        print('%s %s' % (strftime('%Y-%m-%d'), strftime('%H:%M:%S')))
        print("*******", '登录成功 :)')
        print("*******", "状态码{}".format(response))  # 打印状态码
        requests.get(schoolWebLoginURL)
        # print("*******", "正在进入循环检测...\n")
        input("******* 请按下回车来执行新的检测...\n")
