import keyword

# print("ces")
# print(keyword.kwlist)

# if True:
#     print ("True")
# else:
#     print ("False")

# str ="12345"
# print(str)
# print(str+" ces")
# print(str[0:3])
# print(str*2)

# input("\n 按下 enter 键后退出。")

# a, b, c, d = 20, 5.5, True, 4+3j
# print(type(a), type(b), type(c), type(d))

#列表
# list =['abcd', 786 , 2.23, 'runoob', 70.2]
# tinylist = [123, 'runoob']
# print (list)            # 输出完整列表
# print (list[0])         # 输出列表第一个元素
# print (list[1:3])       # 从第二个开始输出到第三个元素
# print (list[2:])        # 输出从第三个元素开始的所有元素
# print (tinylist * 2)    # 输出两次列表
# print (list + tinylist) # 连接列表
# print(list[1:4:2])

#元祖
# tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
# tinytuple = (123, 'runoob')
#
# print (tuple)             # 输出完整元组
# print (tuple[0])          # 输出元组的第一个元素
# print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
# print (tuple[2:])         # 输出从第三个元素开始的所有元素
# print (tinytuple * 2)     # 输出两次元组
# print (tuple + tinytuple) # 连接元组

#集合
# sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu', 'Baidu'}
# print(sites)   # 输出集合，重复的元素被自动去掉
# # 成员测试
# if 'Runoob2' in sites :
#     print('Runoob 在集合中')
# else :
#     print('Runoob 不在集合中')
#集合之间可进行运算

#字典，与集合等不同的是通过键值，而不是偏移,有点像hashmap
# tinydict = {'name': 'runoob',2:1, 'site': 'www'}
# print (tinydict['name'])
# print (tinydict[2])
# print (tinydict.values())

#打印小数点后三位转换成字符串
# a = 5.026536624243638
# print(str(float('%.3f' % a)))
#.join用法，将字符串列表以'x'串联起来
list1 = ['a1','b1','c1']
list2 = [1,2,3]
print(';'.join(list1))
# print(';'.join(list2))
print(list2)
