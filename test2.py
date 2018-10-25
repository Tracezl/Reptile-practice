# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 20:16:59 2018

@author: 赵磊
"""
import requests
from bs4 import BeautifulSoup

url = 'https://beautifulsoup.readthedocs.io/zh_CN/latest/'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.title.name)

"""
url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}

r = requests.post(url, files=files)
r.text
"""
