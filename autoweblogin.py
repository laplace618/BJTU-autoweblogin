import re
import requests
from time import strftime
import time

# URL地址
schoolWebURL = 'http://10.10.42.3'  # 或者是'http://10.10.43.3'

while (True):
    response = requests.get(schoolWebURL)

    # 正则表达式，匹配<title>标签中的内容
    pattern = re.compile('<title>(.*?)</title>', re.S)
    title = re.findall(pattern, response.text)
    title = title[0]  # 将格式转为字符串

    if title == '注销页':
        print('%s %s 连接正常' % (strftime('%Y-%m-%d'), strftime('%H:%M:%S')))
        print("状态码{}".format(response))  # 打印状态码
        time.sleep(5)
        pass

    else:
        user = '20281235'  # 学号
        p = '314618'  # 密码
        t = str(int(round(time.time() * 1000)))  # 毫秒级时间戳
        schoolWebLoginURL = schoolWebURL + '/drcom/login?callback=dr' + t + '&DDDDD=' + user + '&upass=' + p + '&0MKKey=123456&R1=0&R3=0&R6=0&para=00&v6ip=&_=' + t
        print('%s %s 登录成功' % (strftime('%Y-%m-%d'), strftime('%H:%M:%S')))
        print("状态码{}".format(response))  # 打印状态码
        requests.get(schoolWebLoginURL)
