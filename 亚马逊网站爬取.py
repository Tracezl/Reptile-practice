# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:11:03 2018
亚马逊有反爬机制，不允许request库，因此需要修改head头部信息
@author: 赵磊
"""
import requests


url="https://www.amazon.cn/dp/B078FFX8B6/ref=cngwdyfloorv2_recs_0/457-0938929-0373964?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-2&pf_rd_r=MZX39HESNB3X9EKMF160&pf_rd_r=MZX39HESNB3X9EKMF160&pf_rd_t=36701&pf_rd_p=d2aa3428-dc2b-4cfe-bca6-5e3a33f2342e&pf_rd_p=d2aa3428-dc2b-4cfe-bca6-5e3a33f2342e&pf_rd_i=desktop"

try:
    kv={'user-agent':'Mozilla/5.0'}#标准浏览器的标识
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("访问失败")