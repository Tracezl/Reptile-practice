import  pymysql
import  emotionAnalysis
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

def writeProduct(conn,name,price,skuid):
     cursor=conn.cursor()
     sql="INSERT INTO products(pname,price,skuid)values (%s,%s,%s)"
     cursor.execute(sql,(name,price,skuid))
     conn.commit()

def writecomments(conn,skuid,comment):
    cursor=conn.cursor()
    sql="INSERT INTO comments(pid,comments)values (%s,%s)"
    for i in range(len(comment)):
        cursor.execute(sql,(skuid,comment[i]))
        conn.commit()

def getdata(conn):
    cursor=conn.cursor()
    b=[ ]
    sql1="SELECT * FROM products"
    sql2="SELECT * FROM comments where pid=%s"
    try:
        cursor.execute(sql1)
        results=cursor.fetchall()
        for row in results:
            a = {}
            name=row[1]
            price=row[2]
            skuid=row[3]
            a.update(pname=name)
            a.update(pprice=float(price))
            cursor.execute(sql2,(skuid))
            results1=cursor.fetchall()
            c=[]
            for row1 in results1:
                comments=row1[2]
                c.append(comments)
            a.update(comment=c)
            b.append(a)
    except:
        print("Error: unable to fetch data")
    conn.close()
    return b

if __name__ == '__main__':
    conn = pymysql.connect(host="localhost", user='root', password='123456', db='test', charset='utf8')
    b=getdata(conn)
    name=[]
    average=[]
    price=[]
    for  i in range(len(b)):
        name.append(b[i].get('pname'))
        price.append(b[i].get('pprice'))
        result=emotionAnalysis.analySingle(b[i].get('pname'),b[i].get('comment'))
        print(result)
        average.append(result)
    x=[]
    str1=""
    for i in range(len(name)):
        x.append(i+1)
        str1+=str(i+1)+'、'+name[i]+'\n'
    with open('result.txt','w+',encoding='utf-8') as f:
            f.write(str1)
            f.close()
    fig=plt.figure(figsize=(15,10))
    ax=fig.add_subplot(211)
    ax.plot(x, average)
    ax.set_xticks(x)
    ax.set_title(u'情 感 分 析')
    ax.set_xlabel(u'商品名称')
    ax.set_ylabel(u'情 感 程 度')
    ax1 = fig.add_subplot(212)
    ax1.plot(x, price,"r")
    ax1.set_xticks(x)
    ax1.set_title(u'情 感 分 析')
    ax1.set_xlabel(u'商品名称')
    ax1.set_ylabel(u'价格')
    plt.savefig("result.png", dpi=300, bbox_inches='tight')
    plt.show()
    plt.close()
    # comment=['hello','hey']
    # writecomments(conn,'6530217',comment)
    # b=[]
    # a={}
    # a.update(name='mick')
    # a.update(price=1)
    # a.update(comments=['abc','def','ghi','jklmn'])
    # b.append(a)
    # print(b)
# cursor=conn.cursor()
# sql="INSERT INTO students(id,name,gender,city) VALUES (%s,%s,%s,%s)"
# # cursor.execute("delete  from students")
# # conn.commit()
# for i in range(1,100):
#     cursor.execute(sql,((i+1),"郑必成","FEMALE","北京"))
#     conn.commit()
# conn.close()