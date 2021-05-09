#coding:utf-8
import re

cesfile = "ces.txt"
alicefile = 'data/alice.txt'

def alicenum():
    with open(alicefile) as f:
        alice = f.read()
        words = alice.split()
        num = len(words)
        print(num)


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
                # print(time_ori1_)
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

def write(list):
    writefile = 'data/result.txt'
    with open(writefile,'a') as wf:
        for wline in list:
            print(float('%.3f' % wline))
            wf.write(str(float('%.3f' % wline))+'\n')


# alicenum()
# ces()
write([0.30000000000000004, 0.4])