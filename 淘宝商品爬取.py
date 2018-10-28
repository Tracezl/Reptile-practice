# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 13:39:47 2018

@author: 赵磊
"""
import requests
import re
 #将cookies转换成字典形式，zhihu_cookie为保存的cookie文件，跟程序处在同一路径
def get_cookie(cook):
    cookies={}
    for line in cook.split(';'):
        name,value=line.strip().split('=',1)  #1代表只分割一次
        cookies[name]=value 
    return cookies
def getHTMLText(url,kv,cookies):
    try:
        r = requests.get(url,cookies=cookies,headers=kv,timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''
def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print('')
def printGoodsList(ilt):
    tplt = '{:4}\t{:8}\t{:16}'
    print(tplt.format("序号","价格","商品标题"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))
def main():
    goods = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?&q=' + goods
    coo = 't=85db5e7cb0133f23f29f98c7d6955615; cna=3uklFEhvXUoCAd9H6ovaVLTG; isg=BM3NGT0Oqmp6Mg4qfcGPnvDY3-pNqzF2joji8w9SGWTYBu241_taTS6UdFrF3Rk0; miid=983575671563913813; thw=cn; um=535523100CBE37C36EEFF761CFAC96BC4CD04CD48E6631C3112393F438E181DF6B34171FDA66B2C2CD43AD3E795C914C34A100CE538767508DAD6914FD9E61CE; _cc_=W5iHLLyFfA%3D%3D; tg=0; enc=oRI1V9aX5p%2BnPbULesXvnR%2BUwIh9CHIuErw0qljnmbKe0Ecu1Gxwa4C4%2FzONeGVH9StU4Isw64KTx9EHQEhI2g%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; mt=ci=0_0; hibext_instdsigdipv2=1; JSESSIONID=EC33B48CDDBA7F11577AA9FEB44F0DF3'
    cookies = get_cookie(coo)
    """
    for line in coo.split(';'):
        name,value=line.strip().split('=',1)
        cookies[name]=value
        """
    kv = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'}
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' +str(44*i)
            html = getHTMLText(url,kv,cookies)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)
 
main()