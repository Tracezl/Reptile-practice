# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 00:34:58 2018

@author: 赵磊
"""

import sys
import requests
import re
#reload(sys)
#sys.setdefaultencoding('utf8')
import time
import random
import codecs
#import pandas as pd
#from snownlp import SnowNLP


# encoding=utf-8
""" User-Agents """
agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
  ]

cookies = [
        "_T_WM=2d9f4078d7c96e3e03b846ce462ad914; WEIBOCN_FROM=1110006030; WEIBOCN_WM=9006_2001; SSOLoginState=1542473000; ALF=1545065000; SCF=AuRPFg1exQJo3_95jd0nKBJcPpNFpnmPSWxk7yFfmX-HiirTwF-gCwn9wJnK5yfMcoJiJvyM80ZICSbp6Kh5hyU.; SUB=_2A2529DV4DeRhGeNM6VQR9CzKyj2IHXVSF1swrDV6PUNbktAKLVf2kW1NSZy_748A_f_67yrFtYWR4ojcyWKGwt91; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFO_XWaCGks8iqelhBrWnwb5JpX5KMhUgL.Fo-Eeoq7ShzceK22dJLoIpMLxKnLBo-LBo-LxKMLBKeL122ReKnpSntt; SUHB=0IIV0N6KwhgfTZ; MLOGIN=1; M_WEIBOCN_PARAMS=sourceType%3Dqq%26from%3D108B195010%26featurecode%3Dnewtitle%26oid%3D4296083775037324%26luicode%3D20000061%26lfid%3D4296083775037324"
#"SINAGLOBAL=6061592354656.324.1489207743838; un=18240343109; TC-V5-G0=52dad2141fc02c292fc30606953e43ef; wb_cusLike_2140170130=N; _s_tentry=login.sina.com.cn; Apache=5393750164131.485.1511882292296; ULV=1511882292314:55:14:7:5393750164131.485.1511882292296:1511789163477; TC-Page-G0=1e758cd0025b6b0d876f76c087f85f2c; TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; login_sid_t=7cbd20d7f5c121ef83f50e3b28a77ed7; cross_origin_proto=SSL; WBStorage=82ca67f06fa80da0|undefined; UOR=,,login.sina.com.cn; WBtopGlobal_register_version=573631b425a602e8; crossidccode=CODE-tc-1EjHEO-2SNIe8-y00Hd0Yq79mGw3l1975ae; SSOLoginState=1511882345; SCF=AvFiX3-W7ubLmZwXrMhoZgCv_3ZXikK7fhjlPKRLjog0OIIQzSqq7xsdv-_GhEe8XWdkHikzsFJyqtvqej6OkaM.; SUB=_2A253GQ45DeThGeRP71IQ9y7NyDyIHXVUb3jxrDV8PUNbmtAKLWrSkW9NTjfYoWTfrO0PkXSICRzowbfjExbQidve; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFaVAdSwLmvOo1VRiSlRa3q5JpX5KzhUgL.FozpSh5pS05pe052dJLoIfMLxKBLBonL122LxKnLB.qL1-z_i--fiKyFi-2Xi--fi-2fiKyFTCH8SFHF1C-4eFH81FHWSE-RebH8SE-4BC-RSFH8SFHFBbHWeEH8SEHWeF-RegUDMJ7t; SUHB=04W-u1HCo6armH; ALF=1543418344; wvr=6",
#"SINAGLOBAL=6061592354656.324.1489207743838; TC-V5-G0=52dad2141fc02c292fc30606953e43ef; wb_cusLike_2140170130=N; _s_tentry=login.sina.com.cn; Apache=5393750164131.485.1511882292296; ULV=1511882292314:55:14:7:5393750164131.485.1511882292296:1511789163477; TC-Page-G0=1e758cd0025b6b0d876f76c087f85f2c; TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; login_sid_t=7cbd20d7f5c121ef83f50e3b28a77ed7; WBStorage=82ca67f06fa80da0|undefined; WBtopGlobal_register_version=573631b425a602e8; crossidccode=CODE-tc-1EjHEO-2SNIe8-y00Hd0Yq79mGw3l1975ae; cross_origin_proto=SSL; UOR=,,login.sina.com.cn; SSOLoginState=1511882443; SCF=AvFiX3-W7ubLmZwXrMhoZgCv_3ZXikK7fhjlPKRLjog0-14gBQox9IhSK8vZVaZYWsLxUaOWNkudAR9iT6NFJkg.; SUB=_2A253GQ6bDeRhGeNH6FsZ8CjLzj2IHXVUb2dTrDV8PUNbmtAKLWTjkW9NSqHIBUvGapKd6-MQhJTejk3w_ivUUNXZ; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5gYdHWIHRmedh9Nyrij6XN5JpX5K2hUgL.Fo-4e0.RehqNSK22dJLoI0.LxK-L122LB.qLxK-LB.BLBKqLxKMLB.2LBKzLxKnL12-L122LxK.LBK2L12qLxKqLBKqL1KHiqc-t; SUHB=0auwlDzUYulNGs; ALF=1543418442; un=13728408992; wvr=6",
#"SINAGLOBAL=6061592354656.324.1489207743838; TC-V5-G0=52dad2141fc02c292fc30606953e43ef; wb_cusLike_2140170130=N; _s_tentry=login.sina.com.cn; Apache=5393750164131.485.1511882292296; ULV=1511882292314:55:14:7:5393750164131.485.1511882292296:1511789163477; TC-Page-G0=1e758cd0025b6b0d876f76c087f85f2c; TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; login_sid_t=7cbd20d7f5c121ef83f50e3b28a77ed7; WBStorage=82ca67f06fa80da0|undefined; WBtopGlobal_register_version=573631b425a602e8; crossidccode=CODE-tc-1EjHEO-2SNIe8-y00Hd0Yq79mGw3l1975ae; wb_cusLike_5939806751=N; cross_origin_proto=SSL; UOR=,,login.sina.com.cn; SSOLoginState=1511882512; SCF=AvFiX3-W7ubLmZwXrMhoZgCv_3ZXikK7fhjlPKRLjog089iFKjxeT1Oc6cbJkkqgWrnQAuMVukRrJy3898cKIb8.; SUB=_2A253GQ9ADeRhGeNH6FsZ8ynJzz6IHXVUb2eIrDV8PUNbmtAKLVWhkW9NSqG4DzNeLkyPCmJIKq6bXfKXpSRCPLqO; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W50J-rDh2D6-QEqNOZ2NddF5JpX5K2hUgL.Fo-4e0.Re0MfShz2dJLoIEeLxK-LB--L1KeLxK-L1hqLBoMLxKnL1K5LBo8IC281xEfIg5tt; SUHB=0gHiPrbPWNJvao; ALF=1543418511; un=15614187608; wvr=6",
#"SINAGLOBAL=6061592354656.324.1489207743838; TC-V5-G0=52dad2141fc02c292fc30606953e43ef; wb_cusLike_2140170130=N; _s_tentry=login.sina.com.cn; Apache=5393750164131.485.1511882292296; ULV=1511882292314:55:14:7:5393750164131.485.1511882292296:1511789163477; TC-Page-G0=1e758cd0025b6b0d876f76c087f85f2c; TC-Ugrow-G0=e66b2e50a7e7f417f6cc12eec600f517; login_sid_t=7cbd20d7f5c121ef83f50e3b28a77ed7; WBStorage=82ca67f06fa80da0|undefined; WBtopGlobal_register_version=573631b425a602e8; crossidccode=CODE-tc-1EjHEO-2SNIe8-y00Hd0Yq79mGw3l1975ae; wb_cusLike_5939806751=N; wb_cusLike_5939837542=N; cross_origin_proto=SSL; UOR=,,login.sina.com.cn; SSOLoginState=1511882567; SCF=AvFiX3-W7ubLmZwXrMhoZgCv_3ZXikK7fhjlPKRLjog02c5hBW41ia6vpj1cAqbFzE2KCcsXvDxToS_KOeUnwRc.; SUB=_2A253GQ8XDeRhGeNH6FsZ9CjKyjuIHXVUb2ffrDV8PUNbmtAKLU7wkW9NSqGOexL53l1CujvuLpAFNeOEsl05T_5E; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWuISqBnuGqpyxGiWdJ4bOv5JpX5K2hUgL.Fo-4e0.RShqceKM2dJLoI0YLxK-L1K5L1K2LxK.L1KnLBoeLxK-L1K5L1K2LxKqL1-2L1KqLxK.L1KMLBo-LxKMLB.zLB.qLxK-L1hML1-Bt; SUHB=0LcSwyK5XYMzbr; ALF=1543418566; un=13242833134; wvr=6"
]

def readfromtxt(filename):
    file = codecs.open(filename, "r",'utf-8')
    text = file.read()
    file.close()
    return text

def writeintxt(dict,filename):
    output = codecs.open(filename, 'a+','utf-8')
    for i, list in dict.items():
        #comment_str = ""
        #for l in list:
           # comment_str = comment_str + l.__str__().replace('$$','') + "####"
        #output.write(i+"####"+comment_str+'\n')
        for l in list:
            #comment_str = comment_str + l.__str__().replace('$$','') + "####"
            output.write(l+'\n')
                     
    output.close()


user_agent = random.choice(agents)
cookies = random.choice(cookies)
headers = {
    'User-agent' : user_agent,
    'Host' : 'm.weibo.cn',
    'Accept' : 'application/json, text/plain, */*',
    'Accept-Language' : 'zh-CN,zh;q=0.8',
    'Accept-Encoding' : 'gzip, deflate, sdch, br',
    'Referer' : 'https://m.weibo.cn/u/3681837783',
    'Cookie' : cookies,
    'Connection' : 'keep-alive',
}


base_url = 'https://m.weibo.cn/api/comments/show?id='

weibo_id_list = readfromtxt('weibo_id.txt').split('\n')
result_dict = {}
for weibo_id in weibo_id_list:
    try:
        
        i=1
        SIGN = 1
        while(SIGN):
            url = base_url + str(weibo_id) + '&page=' + str(i)
            resp = requests.get(str(url), headers=headers, timeout=200)
            filename=str(weibo_id)+'.txt'
            time.sleep(random.randint(2,3))
            jsondata = resp.json()
            if jsondata.get('ok') == 1:
                SIGN = 1
                i = i + 1
                data = jsondata.get('data')
                #print(jsondata)
                #print(data)
                #print(len(data))
                #print(i)
                record_list = []
                for d in data.get('data'):
                    #print(d)
                    text=re.sub('<.*?>|回复<.*?>:|[\U00010000-\U0010ffff]|[\uD800-\uDBFF][\uDC00-\uDFFF]','',d['text'].replace('$$',''))
                    #print(text)
                    #comment = d.get('text').replace('$$','')
                    #print(comment)
                    #like_count = d.get('like_counts')
                    #user_id = d.get("user").get('id')
                    #user_name = d.get("user").get('screen_name').replace('$$','')
                    #one_record = user_id.__str__()+'$$'+like_count.__str__()+'$$'+user_name.__str__()+'$$'+ comment.__str__()
                    record_list.append(text)
                    #print(record_list)
                with open(filename, 'a', encoding='utf-8') as f:
                    for l in record_list:
                        f.write( str(l) + '\n' )
                    
            else:
                SIGN = 0           
            #SIGN = 0
            #result_dict[weibo_id]=record_list
            #time.sleep(random.randint(2,3))
    except:
        #print(traceback.print_exc())
        result_dict[weibo_id]=record_list
        print(weibo_id)
        print('*'*100)
        pass
print("ok")
#print(result_dict)
#writeintxt(result_dict,'comment1.txt')