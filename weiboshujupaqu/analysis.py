# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 12:06:50 2018

@author: 赵磊
"""

#CalThreeKindomsVq.py
import jieba
txt=open("all.txt","r",encoding="utf-8").read()
#加载过滤词汇
def stopwordslist(filepath):  
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]  
    return stopwords
#加载需要加入的词汇
jieba.load_userdict('words.txt')
words=jieba.lcut(txt)
counts={}
stopwords=stopwordslist('stopWords.txt')
for word in words:
    if len(word)==1:
              continue
    if word not in stopwords:
        if word=="信用分" or word=="芝麻信用" or word=="芝麻分":
              rword="芝麻信用"
        elif word=="医保" or word=="医疗保险":
              rword="医疗保险"
        elif word=="参与" or word=="参加" or word=="参于" or word=="加入" or word=="支持" or word=="建议" or word=="惠民" or word=="互助" or word=="门槛低" or word=="保障" or word=="信任" or word=="创新" :
              rword="积极"
        elif word=="不划算" or word=="拒赔" or word=="骗保" or word=="隐私" or word=="圈钱" or word=="风险" or word=="观望" or word=="管理费":
              rword="消极"      
        elif word=="爸妈" or word=="父母" or word=="家人" or word=="老人":
              rword="家人"
        else:
              rword=word
        counts[rword]=counts.get(rword,0)+1        
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
with open("result.txt", 'a', encoding='utf-8') as f:
    for i in range(50):
         word,count=items[i]
         print("{0:<10}{1:<10}{2:<5}".format(i+1,word,count))
         f.write( "{0:<10}{1:<10}{2:<5}".format(i+1,word,count) + '\n' )

