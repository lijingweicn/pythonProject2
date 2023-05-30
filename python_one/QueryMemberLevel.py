# print('名字','I AM',sep='*')
# print('名字','I AM',end=',')
# print('名字','I AM',sep=',')
# print('名字','I AM',end=',')
# print('名字','I b',end=',')
# import parser
import time
import  random

# ans = random.randint(1,100)

# ans = random.randint(1,100)
# guess = 0
# start = time.time()
# while guess != ans :
#     guess = int(input('guess:'))
#     if guess > ans:
#         print('大了')
#     elif guess < ans:
#         print('小了')
#     else:
#         print('答对了')
# end = time.time()
# game_time = end - start
# print(game_time)
# if game_time <= 20:
#     print('天才')
# elif game_time <= 30:
#     print('一般')
# else:
#     print('太一般')

# from  dateutil import parser
# print(parser.parse(time.ctime()))
# filename = input('filename:')
# a = input('str:')
# a.upper()
# fp = open(filename,'w')
# fp.write(a)
# print('写入')
# fp = open(filename,'r')
# print(fp.read())
#定义lambda实现2数相加
# add = lambda x, y : x+y
# print(add(8,9))
# #定义lambda判断偶数
# is_even=lambda x : x%2 == 0
# print(is_even(6))
# is_even=lambda x : x%2 == 0
# print(is_even(9))
# #使用lambda函数作为key对列表进行排序
# my_list = [(3,2),(6,9),(9,5)]
# print(sorted(my_list,key=lambda x : x[1]))
# #使用lambda函数作为map()的参数进行数据转换
# numbers= [1,3,5,7,9]
# print(list(map(lambda x: x**2,numbers)))

# py语法和常用技巧
# 列表推导式
sq =[x**2 for x in range(1,11)]
print(sq)
#字典推导式
sq = {x: x**2 for x in range(1,11)}
print(sq)
list1 = [1,23,33]
list2 =[6,7,8,9]
pairs = zip(list1,list2)
print(pairs)



















