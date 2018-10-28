# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 13:28:35 2018

@author: 赵磊
"""
import requests
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding =r.apparent_encoding
        return r.text
    except:
        return "访问异常"
    
if __name__=="__main__":
    url="http://www.baidu.com"
    print(getHTMLText(url))
