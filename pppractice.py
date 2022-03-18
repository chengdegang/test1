import pdb
import re
from typing import List

data = "重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，" \
       "不是15600998765，也是110或119，王大锤的手机号才是15600998765。"
data2 = "['[更新日期]05-14  https://www.xxxx.net/xinxi/376489.html  [x'x]xxxx', '[xxx]05-14 http://www.xxxx/xinxi/382934.html  [xx]xxxxx（xxxxx', '[更新日期]05-13  http://www.xxxx.net/xinxi/376344.htmlhttp://d.xxxxxnet/xxxx/d/2021/20210514/xxxx.xlsx  [主题]xxxx.xlsx']"
data3 = "更新日期]05-14  https://www.xxxx.net/xinxi/376489.html  [x'x]xxxx    http://www.xxxx.net/xinxi/376344.htmlhttp://d.xxxxxnet/xxxx/d/2021/20210514/xxxx.xlsx  [主题]xxxx.xlsx"

def re_test():
    mylist = re.findall(r'(?<=\D)1[34578]\d{9}(?=\D)', data)
    mylist_match = re.match(r'(?<=\D)1[34578]\d{9}(?=\D)', data)
    print(mylist)
    print(mylist_match)
    match3 = re.findall(r'http://.*?\.xlsx',data2)
    print(match3)

def strf():
    str = 'abcdefg'
    strr = []
    for i in str:
        strr.append(i)
        print(i)
    strr.reverse()
    print(strr)
    print(''.join(strr))

def strs():
    str = 'abcdefg'
    nstr = str[-1:-10:-1]
    print(nstr)

def xing(*arg):
    # sum = arg +2
    # print(sum)
    print(arg)
    print(type(arg))

def gues():#五位数abcde*9 后 等于edcba ，计算这个五位数
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        if ((a*10000+b*1000+c*100+d*10+e)*9) == e*10000+d*1000+c*100+b*10+a:
                            print(a ,b,c ,d,e)

def yibai():#计算100以内不能被3整除的数
    num = []
    for i in range(100):
        # print(i)
        if i % 3 != 0:
            num.append(i)
    print(num)

def gues3(list,target):#给定一个数，在列表中计算某两个数相加等于它，给出角标
    # list = [2, 3, 5, 6, 10]
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] + list[j] == target:
                return (i,j)
    return (-1,-1)

def strhui(a):#回文数计算
    if str(a) == str(a)[::-1]:
        print("true")
    else:
        print("false")

def longestCommonPrefix(strs) -> str: #计算一个列表中字符的最长公共前缀["ffflsdd","ffokjij"]
    # str1 = 'a'
    # str2 = 'qweqwaeqewf'
    # print(str2.find(str1)) #该方法在str2里查找字符串str1，若存在返回索引角标，若不存在，返回-1

    res = strs[0]
    i = 0
    while i < len(strs):
        while strs[i].find(res) != 0:
            print(f'strs[i]: {strs[i]}')
            print(f'----{res}')
            res = res[0:len(res)-1]
            print(f'res2: {res}')
        i = i + 1
    return res

def isvalid(s):#判断只包含左右括号的字符串是否正确

    stack = [] #存储尾括号，若不为空则
    # a = [1]
    # print(a[-1])
    # print(len(s))
    # pdb.set_trace()
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(')')
        elif s[i] == '{':
            stack.append('}')
        elif s[i] == '[':
            stack.append(']')
        else:
            if stack and stack[-1] == s[i]: # stack and !!!?
                # print(s[i])
                stack.pop()
            else:
                return False
    return not stack

def judge(a,b): #数组里两个数乘积的目标数的两个数 ????
    list = [2,5,6,8,10]
    for i in range(len(list)):
        for j in range(len(list)):
            if list[i] * list[j] == a*b:
                return (i,j)

def zsq(func):
    def wrapTheFunction():
        print("before doing prin ...")
        print(func())
        if func() != "ccc":
            print("invalid name")
        else:
            print("secret key is 123456")
        print("after doing prin ...")
    return wrapTheFunction

@zsq
def prin(info = "ccc" ):
    # print("test prin")
    return info

def link_merge(list1,list2): #合并两个有序链表，按照升序
    new_link = []
    for i in list1:
        new_link.append(i)
    for i2 in list2:
        new_link.append(i2)
    print(sorted(new_link,reverse=False))

def remove_element(list,val): #一个数组及val，原地删除其中的val并返回数组长度
    # print(list)
    # print(len(set(list))) #去重
    for i in list:
        # print(list[i])
        if i == val:
            # print(i)
            list.remove(list[i])
        # else:
        #     continue
    #         list.remove(i)
    list2 =list
    if len(list2) == len(set(list)):
        print(list2)
        print(len(list2))
    else:
        for i in list2:
            if i == val:
                list.remove(list2[i])
    print(list2)
    print(len(list2))

def strStr(haystack: str, needle: str) -> int:#在给定字符串中找到后一个字符串，若没有返回-1，若查找字符串为空返回0
    print(haystack.find(needle))

def maxSubArray( nums: List[int]) -> int: #在整数数组中找到具有最大和的连续子数组（子数组最少包含一个元素）
    pre = 0
    res = nums[0]
    for i in range(len(nums)):
        pre = max(nums[i],pre + nums[i])
        # print(pre)
        res = max(pre,res)
    return res
        # print(i)
    #？？？？？？？？？？？？？？？

def lengthOfLastWord( s: str) -> int: #计算字符串中最后一个单词的长度
    strlist = s.split(" ")
    print(strlist)
    long = len(strlist) - 1
    for i in range(len(strlist)):
        # print(strlist[i])
        if strlist[long] != '':
            print(len(strlist[long]))
            break
        else:
            long = long - 1

def plusOne( digits: List[int]) -> List[int]:  #在非空数组上加1
    lastone =  digits[-1] + 1
    res = []
    for i in range(len(digits)-1):
        res.append(digits[i])
    if lastone <= 9:
        res.append(lastone)
    else:
        1
    print(res)

if __name__ == "__main__":
    # prin = zsq(prin)  #装饰器的一种运行方式
    # prin()

    plusOne([9])
    # lengthOfLastWord("   fly me   to   the moon  ")
    # maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) #？？？
    # strStr('haystack','ays') # needle
    # remove_element([0,1,2,2,3,0,4,2],val=3)
    # link_merge([1,2,4],[1,3,4])
    # print(longestCommonPrefix(["ffflxs","ffflswww","ffwewe"]))
    # print(isvalid("()"))
    # test(a)
    # print(gues3([2, 3, 5, 6, 10],8))
    # gues()
    # xing(3,2,4)
    # yibai()
    # strs()
    # strf()
    # re_test()
    # print(judge(2,2))

