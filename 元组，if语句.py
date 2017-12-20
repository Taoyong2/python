# coding:utf-8
# author: Tao yong
# Python

#元组：类似于列表，元素无法修改，不能给元素赋值
#元组用于存放数值无法更改的元素
dimensions=(200,50)
#for循环遍历元组
for dimension in dimensions:
    print(dimension)

#可以给元组的变量赋值，即可以重新定义整个元组
dimensions=(400,100)
for dimension in dimensions:
    print(dimension)

#例1：遍历列表cars并打印，对于bmw元素所有字母大写，其他元素首字母大写
cars=['aodi','bmw','toyota','subaru']
for car in cars:
    #检查字符串是否相等不区分大小写
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

#例2：打印n以内的所有素数的列表
def prime(n):
    l=[]
    for number in range(1,1+n):
        if number==1:
            continue
        elif number==2:
            l.append(number)
        else:
            if 0 not in [number%i for i in range(2,number)]:
                l.append(number)
    print(l)

#关键字or和and检查多个条件 ,and的优先级大于or
#in关键字 检查特定值是否在列表中
#not in关键字 件查特定值是否不在列表中
a=list(range(0,20))
for number in a:
    if (number%2==0 or number%3==0) and number%5==0:
        print(number)
    if number in range(3,7):
        print(number)
    if number not in range(1,19):
        print(number)

'''
    1.if语句的结构
    if（判断）：
    elif（判断）：
    ……
    elif（判断）：
    else：
    满足第一个if语句时，将会跳过剩余语句
    除了if语句，其余都可以省略  
    2.if语句处理列表
        1.检查特殊元素是否在列表中
        2.确定列表是否为空
'''
#if检查到空列表时，返回False，检查到非空列表时，返回True
list_a=[]
if list_a:
    print('a')
else:
    print('b')
