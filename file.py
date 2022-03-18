#coding:utf-8
import os
import re
from collections import Counter

cesfile = "ces.txt"
alicefile = 'data/alice.txt'

#统计文件中的单词数并得出出现频率最高的十个单词
def alicenum():
    with open(alicefile) as f:
        alice = f.read()
        words = alice.split()
        num = len(words)
        print(num)
    # print(words.count('it'))
    c = Counter(words)
    print(c)
    print(c.most_common(10))

    # dic = {}


#正则提取文件中的数据并处理
def ces():
    with open(cesfile) as ces:
        #1读取返回所有内容
        # read = ces.read()
        #2返回一行
        # read = ces.readline()
        #3列表内返回所有，与1类似，常用此
        read = ces.readlines()
        # print(read)
        pline = ''
        time1 = []
        time2 = []
        for line in read:
            # 遍历每行添加处理,把每行加到后面
            # pline +=  line.rstrip()
            #打印每一行
            # print(line.strip())
            #找到两个时间并相减
            if 'time1' in line:
                # time_ori1 = line.split('time1')
                #正则提取time1与s之间的数
                time_ori1 = re.findall(r"time1=(.+?)s", line)
                #去掉列表括号
                time_ori1_ = ''.join(time_ori1)
                # print(time_ori1)
                time1.append(time_ori1_)
            if 'time2' in line:
                # time_ori1 = line.split('time1')
                #正则提取time1与s之间的数
                time_ori2 = re.findall(r"time2=(.+?)s", line)
                time_ori2_ = ''.join(time_ori2)
                # print(time_ori2_)
                time2.append(time_ori2_)
    num_time1 = list(map(float, time1))
    num_time2 = list(map(float, time2))
    print(num_time1)
    print(num_time2)

    #处理拿到的time1、2
    value = [num_time2[i] - num_time1[i] for i in range(len(num_time1))]
    print(value)

    #检查输入的数是否在读取的文件里面
        # print(pline)
        # inp = input("输入一个str: \n")
        # if inp in pline:
        #     print("in")
        # else:
        #     print("out")

#处理列表中的小数，并统一
def write(list):
    writefile = 'data/result.txt'
    with open(writefile,'a') as wf:
        for wline in list:
            print(float('%.3f' % wline))
            wf.write(str(float('%.3f' % wline))+'\n')

dirf = '/Users/jackrechard/PycharmProjects/testexcel/file'

#遍历某个文件夹下的所有文件
def dir(file):
    # root 表示当前正在访问的文件夹路径
    # dirs 表示该文件夹下的子目录名list
    # files 表示该文件夹下的文件list
    for root, dirs, files in os.walk(file):
        for f in files:
            #判断是否存在.xlsx的文件
            if '.xlsx' in f:
                #打印文件名
                # print(f)
                #打印文件路径
                print('----------关注以下数据----------')
                print(os.path.join(root, f))

            # print(os.path.join(root,f))
        # for d in dirs:
        #     print(os.path.join(root, d))
direct = '/Users/jackrechard/PycharmProjects/testexcel/file/test.txt'
#测试os的分离文件与扩展名
def ostest():
    result1 = os.path.splitext(direct)
    if '.txt' in result1[1] :
        print(result1)
        print('find it')

def qiepian():
    data = ",b'/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAIBAQEBAQIBAQECAgICAgQDAgICAgUEBAMEBgUGBgYFBgYGBwkIBgcJBwYGCAsICQoKCgoKBggLDAsKDAkKCgr/"
    data2 = '666'
    data2 = f'123{data2[0:]}'
    print(data2)

alicenum()
# ces()
# write([0.30000000000000004, 0.4])
# dir(dirf)
# ostest()
# qiepian()