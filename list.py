import random
import re

listnew =['[<li><em>05-14</em><a href="http://www.shiyebian.net/xinxi/376489.html" target="_blank">2021年杭州住房公积金管理中心桐庐分中心招聘编外人员公告</a></li>]',
'[<li><em>05-14</em><a href="http://www.shiyebian.net/xinxi/376488.html" target="_blank">2021年杭州市桐庐县商务局（桐庐迎春商务区管理委员会）招聘编外人员公告</a></li>]',
'[<li><em>05-13</em><a href="http://www.shiyebian.net/xinxi/376344.html" target="_blank">2021年杭州市桐庐县行政服务中心招聘编外人员公告</a></li>]']

listold =[
'[<li><em>05-14</em><a href="http://www.shiyebian.net/xinxi/376488.html" target="_blank">2021年杭州市桐庐县商务局（桐庐迎春商务区管理委员会）招聘编外人员公告</a></li>]',
'[<li><em>05-13</em><a href="http://www.shiyebian.net/xinxi/376344.html" target="_blank">2021年杭州市桐庐县行政服务中心招聘编外人员公告</a></li>]',
'[<li><em>05-13</em><a href="http://www.shiyebian.net/xinxi/376342.html" target="_blank">2021年杭州市桐庐县林业水利局招聘编外人员公告</a></li>]',
'<li><em>04-26</em><a href="http://www.shiyebian.net/xinxi/374685.html" target="_blank">2021年杭州市富阳区事业单位招聘报名条件及招考范围</a></li>']

a='[<li><em>05-14</em><a href="http://www.shiyebian.net/xinxi/376489.html" target="_blank">2021年杭州住房公积金管理中心桐庐分中心招聘编外人员公告</a></li>]'

listre = ['data1 www.baidu.com','data2 www.ces.com']

liststr = ['123','中国','ces']

# if a in listold:
#     print('true')
# else:
#     print('false')
listjoin = ['1','2','3']
listjoin2 = ['5','6']
listjoin3 = [[5],[6]]

def choicenotsame():
    a = [x for x in listnew if x in listold]  # 两个列表表都存在
    b = [y for y in (listnew + listold) if y not in a]

    print(f'same is:{a}')
    print(f'notsame is:{b}')
    c = []
    # for z in b:
    #     if z in listnew:
    #         c.append(z)

    for z in b:
        if z in listnew and z in listold :
            continue
        else:
            if z in listnew:
                c.append(z)
    print(f'final is: {c}')

def join():
    listjoin_after = ','.join(listjoin3)
    print(listjoin_after)

#for循环判断
def judge2(listnew,listold):
    c = []
    for z in listnew:
        if z in listold:
            continue
        else:
            c.append(z)

    print(c)
    return c

def ces_meg():
    mesg_2 = ''
    # mesg_2 = mesg_2+ listre[0] + '\n'
    # mesg_2 = mesg_2 + listre[1] + '\n'
    for i in range(len(listre)):
        mesg_2 = mesg_2 + listre[int(i)] + '\n'

    print(mesg_2)

def cespanduan():
    for i in liststr:
        if "中" in i:
            print(i)

def xunhuan():
    data1 = ['data1','data2','data3']
    data2 = ['data21','data22']
    for i in range(3):
        print(data1[i])
        print(random.choice(data2))

def quchong():
    list1 = [['序号', 'title1', 'title1', 'title2', 'title3', 'title4', 'title5', 'title6', 'title7', 'title8', 'title9', 'title10_value'], ['序号', 'title1', 'title1', 'title2', 'title3', 'title4', 'title5', 'title6', 'title7', 'title8', 'title9', 'title10_value'], [2, '数据dw1', '数据dw2', '数据cz1', '数据gw2', '数据type1', 1, '/', '数据sf', '数据yq1', '数据2yq_2', '数据zy2_1'], [5, '数据dw1', '数据dw3', '数据cz2', '数据gw5', '数据type2', 1, '/', '数据sf', '数据yq1', '数据2yq_2', '数据zy1_1'], [2, '数据dw1', '数据dw2', '数据cz1', '数据gw2', '数据type1', 1, '/', '数据sf', '数据yq1', '数据2yq_2', '数据zy2_1'], [5, '数据dw1', '数据dw3', '数据cz2', '数据gw5', '数据type2', 1, '/', '数据sf', '数据yq1', '数据2yq_2', '数据zy1_1']]
    # list2 = list(set(list1))
    list3 = [1,0,0,3,7,7,5]
    # list4 = list(set(list3))
    a = ['序号', 'title1', 'title1', 'title2', 'title3', 'title4', 'title5', 'title6', 'title7', 'title8', 'title9', 'title10_value']
    # print(list4)
    b = []
    for element in list1:
        # print(element)
        if element not in b:
            b.append(element)
    print(b)
    # if a in list1:
    #     print('in')

data = ['<a href="http://www.shiyebian.net/sitemap.html" target="_blank">网站地图</a>, <a href="http://www.shiyebian.net/sitemap.xml" target="_blank">XML地图</a>']
data2 = '[a,b]'
data3= ['[<a href="http://www.shiyebian.net/sitemap.html" target="_blank">网站地图</a>', ' <a href="http://www.shiyebian.net/sitemap.xml" target="_blank">XML地图</a>', ' <a href="http://www.shiyebian.net/xinxi/" target="_blank">最新文章</a>', ' <a href="http://www.shiyebian.net"><img alt="事业单位招聘考试网" height="73" src="http://www.shiyebian.net/images/logo.gif" width="250"/></a>', ' <a class="nobg" href="http://www.shiyebian.net">首页</a>', ' <a href="http://bbs.shiyebian.net" target="_blank">资料论坛</a>', ' <a href="http://www.shiyebian.net/ask/">问题咨询</a>', ' <a href="http://www.shiyebian.net/ziliao/">资料大全</a>', ' <a href="http://www.shiyebian.net/shiti/">试题题库</a>', ' <a href="http://www.shiyebian.net/shishi/">时事政治</a>', ' <a href="http://www.shiyebian.net/ribao/">招聘日报</a>', ' <a href="http://www.shiyebian.net/ziliao/xingce.html">行测资料</a>', ' <a href="http://www.shiyebian.net/ziliao/shenlun.html">申论资料</a>', ' <a href="http://www.shiyebian.net/ziliao/mianshi.html">面试资料</a>', ' <a href="http://www.shiyebian.net/ggjc.html">公基资料</a>', ' <a href="http://www.shiyebian.net/">首页</a>', ' <a href="http://www.shiyebian.net/zhejiang/">浙江事业单位招聘网</a>', ' <a href="http://www.shiyebian.net/zhejiang/hangzhou/">杭州事业单位招聘网</a>', ' <a href="/zhejiang/">浙江事业单位招聘网</a>', ' <a href="/zhejiang/hangzhou/">杭州</a>', ' <a href="/zhejiang/ningbo/">宁波</a>', ' <a href="/zhejiang/wenzhou/">温州</a>', ' <a href="/zhejiang/jiaxing/">嘉兴</a>', ' <a href="/zhejiang/huzhou/">湖州</a>', ' <a href="/zhejiang/shaoxing/">绍兴</a>', ' <a href="/zhejiang/jinhua/">金华</a>', ' <a href="/zhejiang/quzhou/">衢州</a>', ' <a href="/zhejiang/zhoushan/">舟山</a>', ' <a href="/zhejiang/taizhou/">台州</a>', ' <a href="/zhejiang/lishui/">丽水</a>', ' <a href="http://www.shiyebian.net" target="_blank">事业单位招聘网</a>', ' <a class="infotextkey" href="http://www.shiyebian.net/zhejiang/tongluxian/" target="_blank">桐庐县</a>', ' <a href="http://d.shiyebian.net/shiyebian/d/2021/20210514/杭州住房公积金管理中心桐庐分中心公开招聘编外人员计表b.docx">杭州住房公积金管理中心桐庐分中心公开招聘编外人员计表.docx</a>', ' <a href="http://d.shiyebian.net/shiyebian/d/2021/20210514/杭州住房公积金管理中心桐庐分中心公开招聘编外人员报名表.xlsx">杭州住房公积金管理中心桐庐分中心公开招聘编外人员报名表.docx</a>', ' <a href="http://www.shiyebian.net/xinxi/376488.html">2021年杭州市桐庐县商务局（桐庐迎春商务区管理委员会）招聘编外人员公告</a>', ' <a href="http://www.shiyebian.net/xinxi/376755.html">2021年浙江省审计科学研究所招聘公告</a>', ' <a href="http://www.shiyebian.net/xinxi/376488.html" target="_blank">2021年杭州市桐庐县商务局（桐庐迎春商务区管理委员会）招聘编外人员公告</a>', ' <a href="http://www.shiyebian.net/xinxi/376487.html" target="_blank">2021年宁波市慈溪财政局编外用工人员招聘公告</a>', ' <a href="http://www.shiyebian.net/xinxi/376486.html" target="_blank">2021年宁波市水利局直属事业单位招聘高层次人才公告</a>', ' <a href="http://www.shiyebian.net/xinxi/376485.html" target="_blank">2021年浙江纺织服装职业技术学院招聘高层次高技能人才公告</a>', ' <a href="http://www.shiyebian.net/xinxi/376459.html" target="_blank">2021年宁波职业技术学院招聘教师公告</a>', ' <a href="http://www.shiyebian.net/xinxi/376376.html" target="_blank">2021上半年舟山医院合同制卫生专业技术人员招聘公告</a>', ' <a href="http://www.shiyebian.net/xinxi/376346.html" target="_blank">2021年台州市住房和城乡建设局下属单位招聘编制外用工公告</a>', ' <a href="http://www.shiyebian.net/xinxi/376345.html" target="_blank">2021年农工党嘉兴市委会招聘岗位合同工公告（浙江）</a>', ' <a href="http://www.shiyebian.net/xinxi/376344.html" target="_blank">2021年杭州市桐庐县行政服务中心招聘编外人员公告</a>', ' <a href="http://www.shiyebian.net/xinxi/376343.html" target="_blank">2021年温州市瓯海区温瑞塘河工程建设中心招聘公告</a>]']

excel_urls = []
for i in data3:
    # print(i)
    excel_url = re.findall(r'http.*.xlsx', i)
    excel_url = ''.join(excel_url)
    if len(excel_url) > 0:
        excel_urls.append(excel_url)

a = ['a','b','c','b','b','b']
def remove():
    # a.remove('b')
    print(len(a))
    # for i in a:
    #     if 'b' == i:
    #         a.remove('b')
    print(list(filter(lambda x: x != 'b', a)))
    # print(a)

db = ["['A1324','iPhone 3G (国行)']", "['A1303','iPhone 3GS']"]
def replace():
    for i in db:
        # res = i.replace('"', "")
        # print(res)
        print(i)

def dic():
    words = [
        'my', 'skills', 'are', 'poor', 'I', 'am', 'poor', 'I',
        'need', 'skills', 'more', 'my', 'ability', 'are',
        'so', 'poor'
    ]
    dict1 = {}
    for i in words:
        if i not in dict1.keys():
            dict1[i] = words.count(i)
    print(dict1)
    print(sorted(dict1.values(),reverse=True))

    # dic = {1:'ces',2:'ces2',3:'ces3'}
    # print(dic.values())

# dic()
# replace()
# remove()
# print(excel_urls)
# print(data3)

# print(listjoin)
# join()
# choicenotsame()
# result = judge2(listnew,listnew)
# if len(result) > 0 :
#     print("更新了")
# else:
#     print("没有更新")

# ces_meg()
# cespanduan()
xunhuan()
# quchong()