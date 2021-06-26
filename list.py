
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

# print(listjoin)
# join()
# choicenotsame()
# result = judge2(listnew,listnew)
# if len(result) > 0 :
#     print("更新了")
# else:
#     print("没有更新")

ces_meg()