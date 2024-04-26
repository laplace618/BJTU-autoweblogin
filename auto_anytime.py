import requests
import datetime
import time
import re
from time import strftime


# URL地址
schoolWebURL1 = 'http://10.10.42.3'
schoolWebURL2 = 'http://10.10.43.3'
user = 'XXXXXXXX'  # 学号
p = 'XXXXXXXX'  # 密码

while (True):
    now_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        response = requests.get(schoolWebURL1)
    except requests.exceptions.RequestException:
        print(now_date, "\n*******", '连接异常 :(')
        print("*******", '网络连接已断开，请检查您的连接 :()')
        time.sleep(60)  # 等待60秒后重新尝试连接
        continue
    # 正则表达式，匹配<title>标签中的内容
    pattern = re.compile('<title>(.*?)</title>', re.S)
    title = re.findall(pattern, response.text)
    title = title[0]  # 将格式转为字符串

    if title == '注销页':
        print(now_date, "\n*******", '连接正常 :)')
        print("*******", "状态码{}".format(response))  # 打印状态码
        # print("*******", "正在等待下一次检测...\n")
        input("******* 请按下回车来执行新的检测...\n")
        pass

    else:
        t = str(int(round(time.time() * 1000)))  # 毫秒级时间戳
        schoolWebLoginURL = schoolWebURL1 + '/drcom/login?callback=dr' + t + '&DDDDD=' + user + '&upass=' + p + '&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&_=' + t
        requests.get(schoolWebLoginURL)
        print('%s %s' % (strftime('%Y-%m-%d'), strftime('%H:%M:%S')))
        print("*******", '登录成功 :)')
        print("*******", "状态码{}".format(response))  # 打印状态码
        # print("*******", "正在进入循环检测...\n")
        input("******* 请按下回车来执行新的检测...\n")
        break
