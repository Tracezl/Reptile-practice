n# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:02:29 2018

@author: 赵磊
"""
import requests
import re
 
#将cookies转换成字典形式，zhihu_cookie为保存的cookie文件，跟程序处在同一路径
def get_cookie():
    with open('zhihu_cookie.txt','r') as f:
        cookies={}
        for line in f.read().split(';'):
            name,value=line.strip().split('=',1)  #1代表只分割一次
            cookies[name]=value 
        return cookies
 
s = requests.Session()
url = 'http://www.zhihu.com/#signin'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
    'Accept':'*/*',
    'Accept-Language':'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding':'gzip, deflate, br',
    'Referer':'https://www.zhihu.com/'
    }
req2 = s.get(url, headers = headers, cookies = get_cookie(), verify=False)
print(req2.encoding)
html = req2.content

#bytes.decode(html) 
#print(html);
#将获取到的页面源码写入zhihu.html文件中
with open('zhihu.html','wb') as fl:
    fl.write(html)