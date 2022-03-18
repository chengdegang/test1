import function as fu

# print("hello")

# print(fu.inputgame())

# a_list = [[1], [2], [3]]
# b = [[11], [22], [33]]
a = ['1.5', '2', '3']
b = ['11', '22', '33']
num_a = list(map(float, a))
num_b = list(map(int, b))
# a = [1, 2, 3]
# b = [11, 22, 33]
# c = [b[i] - a[i] for i in range(len(a))]
# c = [num_b[i] - num_a[i] for i in range(len(num_a))]
# print(c)
# print(num_a)


# print(numbers)

# a[0] = 3
# print(a)

# a_list=['monday']
# a_list=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
# a_list_ = ''.join(a_list)
# print(a_list_)
# print(''.join(a_list))
# print(a_list)
# print("\r")
# b_tuple=('monday','tuesday','wednesday','thursday','friday','saturday','sunday')
# print(' '.join(b_tuple))

result_suc = 0
result_fail = 0
dataxy = {'code': '00000000', 'msg': '成功', 'result': {'algEncodingType': 0, 'algEncodingData': 'EAj3/dAJEMHMy5f67ycYECAAKlAKABCAgP7///////8BGhsZAAAAAAAAAIAZAAAAAAAAAAAZAAAAAAAAAIAiJBkAAAAAAAAAABkAAAAAAAAAABkAAAAAAAAAABkAAAAAAADwPzIA', 'algCode': 1, 'protobufEncodingData': 'EAj3/dAJEMHMy5f67ycYECAAKlAKABCAgP7///////8BGhsZAAAAAAAAAIAZAAAAAAAAAAAZAAAAAAAAAIAiJBkAAAAAAAAAABkAAAAAAAAAABkAAAAAAAAAABkAAAAAAADwPzIA'}}
algcode = str(dataxy['result']['algCode'])
print(algcode)
if algcode == '1':
    result_suc = result_suc + 1
elif '16' in algcode:
    result_fail = result_fail + 1

print(f'result_suc:{result_suc}')
print(f'result_fail:{result_fail}')