from snownlp import SnowNLP
import matplotlib.pyplot as pl
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
import  os
# import pylab as pl
# txt = open("comment.txt","r",encoding="utf-8")
# text = txt.readlines()
# txt.close()
# print('读入成功')
def analySingle(name,text):
    senti_score = []
    all = 0
    for i in text:
        a1 = SnowNLP(i)
        a2 = a1.sentiments
        senti_score.append(a2)
        all += a2
    x = range(1, len(senti_score) + 1)
    pl.plot(x, senti_score, label='单用户')
    average=all / len((senti_score))
    y = [average] * len((senti_score))
    pl.plot(x, y, 'r', label='平均')
    pl.legend(bbox_to_anchor=(1, 0), loc=3, borderaxespad=0)
    pl.title(u'情 感 分 析')
    pl.xlabel(u'评 论 用 户')
    pl.ylabel(u'情 感 程 度')
    path='./Data/'
    Isexist=os.path.exists(path)
    if  not Isexist:
        os.mkdir(path)
    pl.savefig(path+name.replace('/','') + ".png", dpi=300, bbox_inches='tight')
    # pl.show()
    pl.close()
    return average
# analySingle("sss",text)
# analySingle("aaa",text)

