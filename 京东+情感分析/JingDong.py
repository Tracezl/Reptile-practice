import  requests
from  bs4 import  BeautifulSoup
import json
import time
import BlackBoard
import pymysql
headers={
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'areaId=22; PCSYCityID=1930; shshshfpa=a8e2244a-78fb-ac48-ac9c-86b8ec39305b-1555425432; ipLoc-djd=1-72-2799-0; jwotest_product=99; unpl=V2_ZzNtbUUHSxQgDxRcLE5fUmIFQltKURMcJw8TUS5OXgJnU0dfclRCFX0UR1FnGVUUZwcZXEFcQxBFCEdkexhdBGYCEFpBU3NXK14YECdSbDVkAyJdQ2dAFHUJRFF%2bHlQNVzMVbXJnQiV0OEdkMHddSGQCElxAUkYSfQB2VUsa; __jdv=122270672|123.sogou.com|t_1000003625_sogoumz|tuiguang|6a90d6c9ff2f47a797a8c6d4df361ad3|1555570933472; _gcl_au=1.1.836336165.1555570950; shshshfp=3672fa65a84eb4c2cd4e8447e6f9bb83; shshshsID=9901671416c9854ee1ef619de1572d42_7_1555571475081; shshshfpb=pa10Swq0y2SdyzGthEStKJA%3D%3D; __jda=122270672.2010344699.1553690406.1555425432.1555570933.2; __jdb=122270672.7.2010344699|2.1555570933; __jdc=122270672; 3AB9D23F7A4B3C9B=MQZIICQHDDZ3L75TDTOB4ZKMX3RX26XUGNK7XOZKXPYAHXWLFX3LVLQICBXQRN4WM6Y2AOZ5ZTZN5MTY5ZLB7K3YSQ; __jdu=2010344699; JSESSIONID=4F6B06FC670803AF038424F2471781EE.s1',
    'Host':'club.jd.com',
    'Referer':'https://item.jd.com/4461439.html',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
headers1={
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding':'gzip, deflate, sdch, br',
    'accept-language':'zh-CN,zh;q=0.8',
    'cache-control':'max-age=0',
    'cookie':'areaId=22; PCSYCityID=1930; shshshfpa=a8e2244a-78fb-ac48-ac9c-86b8ec39305b-1555425432; ipLoc-djd=1-72-2799-0; qrsc=3; unpl=V2_ZzNtbUdVShx3WE5cckkPBWIDFg5KVUBFIQsRVHJODAxiBRQIclRCFX0UR1FnGVUUZwsZXUFcQxJFCEdkeBBVAWMDE1VGZxBFLV0CFSNGF1wjU00zQwBBQHcJFF0uSgwDYgcaDhFTQEJ2XBVQL0oMDDdRFAhyZ0AVRQhHZHgYXARlBhdaSl9zJXI4dmR9GVUFZQQiXHJWc1chVEBReBBcAyoAE11DVUYQcgBOZHopXw%3d%3d; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_43883a998ab1415b932ae2f18fa8477d|1555585935112; mt_xid=V2_52007VwATUlxaV18YQRFsDDNUEFJVXlpGHBsbDBliCxBUQQhSXh5VSw4FM1BGAF1RVV5MeRpdBW8fE1dBWFtLH0ESXA1sAxRiX2hSah1NHF4BYQUVUG1YV1wY; _gcl_au=1.1.1778836492.1555586357; __jda=122270672.2010344699.1553690406.1555577910.1555585426.4; __jdb=122270672.41.2010344699|4.1555585426; __jdc=122270672; shshshfp=ef61c4da3dd26f18e57fe6ddd2b8ac55; shshshsID=3b0955093eafbfd24802b9a169e61203_40_1555586497024; shshshfpb=pa10Swq0y2SdyzGthEStKJA%3D%3D; rkv=V0700; xtest=3406.cf6b6759; __jdu=2010344699; 3AB9D23F7A4B3C9B=MQZIICQHDDZ3L75TDTOB4ZKMX3RX26XUGNK7XOZKXPYAHXWLFX3LVLQICBXQRN4WM6Y2AOZ5ZTZN5MTY5ZLB7K3YSQ',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
}
url='https://search.jd.com/Search?keyword=耳机&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&click=0'
result=requests.get(url,headers=headers1)
content=result.content.decode('utf-8')
neirong=BeautifulSoup(content,'lxml')
ul=neirong.find(attrs={'class':'gl-warp clearfix'})
lis=ul.find_all('li',{'data-sku':True})
proxies = {'https': 'https://113.108.242.36:47713'}
conn = pymysql.connect(host="localhost", user='root', password='123456zbc', db='test', charset='utf8')
for i in range(len(lis)):
    skuid=lis[i].attrs['data-sku']
    name=""
    price=lis[i].find(attrs={'class':'p-price'}).find('i')
    price1=0
    if  len(price.text)>0:
        price1=price.text
    else:
        price=lis[i].find('strong',{'data-price':True})
        price1=price.attrs['data-price']
    for j in range(100):
        if j<=90:
            url = 'https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv106&productId=' + str(skuid) + '&score=0&sortType=5&page=' \
                      + str(j) + '&pageSize=10&isShadowSku=0&rid=0&fold=1'
        else:
            url = 'https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv106&productId=' + str(skuid) + '&score=1&sortType=5&page=' \
                     + str(j%10) + '&pageSize=10&isShadowSku=0&rid=0&fold=1'
        content1=requests.get(url,headers=headers)
        begin=content1.text.find('(')+1
        data0=content1.text[begin:-2]
        data1=json.loads(data0)
        str1 = ""
        comments=[]
        for k in range(len(data1['comments'])):
            if(k==0 and j==0):
                name=data1['comments'][k]['referenceName']
                # str1+=str(i+1)+'、'+data1['comments'][k]['referenceName']+'\n'
                # print(str(i+1)+'、'+data1['comments'][k]['referenceName'])
            comments.append(data1['comments'][k]['content'].replace('\n',''))
        print('第' + str(i) + '个商品' + '第' + str(j) + '页已完成')
        if j==0:
            BlackBoard.writeProduct(conn,name,price1,skuid)
        BlackBoard.writecomments(conn,skuid,comments)
            # str1+=data1['comments'][k]['content'].replace('\n','')+'\n'
        # with open('./product.txt', 'a+', encoding='utf-8') as f:
        #      f.write(str1)
        #      f.close()
        time.sleep(5)
    print()
conn.close()