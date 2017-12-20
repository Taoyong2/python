# coding:utf-8
# author: Tao yong
# Python

frist_name='Tao'
last_name='yong'
full_name=frist_name+last_name
#字符串合并不会自动加空格符
#连续打印多个字符串，字符串之间会自动加空格
print(full_name)
print(frist_name,last_name)

#\n为换行符 \t为制表符
print('language:\n\tPython\n\tC\n\tJavascript')

#rstrip()方法消除字符串末尾多余的空格
#lstrip()方法消除字符串开头多余的空格
favorite_language='  python   '
print(favorite_language.rstrip(),'1')
print(favorite_language.lstrip())

#整型不能和字符串合并，需要先进行类型转换
age=23
message='Happy '+str(age)+'rd Brithday'
print(message)

#列表元素的提取，字符串的title方法，返回所有字符串首字母大写
#字符串的upper方法，返回所有字符大写,lower方法，返回所有字符小写
language=['python','C','C#','Java']
print(language[0].upper())
print(language[0].title())
print(language[3].lower())
#列表添加元素append方法和修改元素
language[0]='C++'
language.append('Python')

#删除列表中元素的三种方法
#用del关键字删除列表元素
del language[2]
print(language)
#用pop方法弹出列表中任意元素，默认弹出最后一个元素
poped_language=language.pop()
pop_frist_language=language.pop(1)
print(pop_frist_language)
print(poped_language)
print(language)
#根据值使用remove方法删除元素
language.remove('C++')
print(language)

#列表的排序方法总结
#sort方法对列表进行永久性排序
car=['dazhong','xiandai','qirui','aodi']
car.sort()
print(car)
#sort的reverse参数为True时进行倒序排序
car.sort(reverse=True)
print(car)
#sorted函数对列表进行临时性排序，不改变列表原有顺序
print(sorted(car))
#函数reverse()永久性反转列表排列顺序
reversed(car)
print(car)

#len()函数查看列表元素的长度
print(len(car))

'''
    对于一个长度为n的列表a而言，第一个元素为a[0],最后一个元素为a[n-1]
    或者最后一个元素为a[-1],第一个元素为a[-n+1]
'''

#遍历列表
for i in car:
    print(i)

#用range函数打印一系列函数,包括第一个数字，不包括最后一个数字,
for value in range(1,5):
    print(value)

#range函数第三个参数是步长
for value in range(2,11,2):
    print(value)

#用list函数将range直接转换为列表
numbers=list(range(9,15))
print(numbers)

#例1：计算从1+2^2+3^3+4^4+……+n^n的和
def function(n):
    sum=0
    for number in range(1,n+1):
        sum+=number**number
    return sum

#列表解析例1
def function_t(n):
    a=[value**value for value in range(1,n+1)]
    return sum(a)

#例2：创建一个1到n的平方的列表
def square_function(n):
    a=[]
    for number in range(1,n+1):
        a.append(number*number)
    return a

#列表解析例2
def square_function_t(n):
    squares=[value*value for value in range(1,n+1)]
    return squares

#min max sum函数找到列表的最大值，最小值和计算列表的和
b=[]
for number in range(1,10,2):
    b.append(number)
print(min(b),max(b),sum(b))

#例3：列表解析法生成前十个数的立方的列表
cubes=[number**3 for number in range(1,11)]


#使用列表切片
#两个参数，包含第一个参数起始位，不包含第二个参数终止位，最后一个参数为-1
print(cubes[0:3],'\n',cubes[:5],'\n',cubes[3:9],'\n',cubes[7:],'\n',cubes[-4:-1])
#用负数参数获取列表的最后n位元素print(cubes[-n:])
print(cubes[-3:])
#遍历列表切片
for number in cubes[-7:-4]:
    print(number)

#列表的相加
a=cubes[0:5]+cubes[5:11]
print(a)
#列表的复制,更改列表b不会改变原列表
#若写成b=cubes,则改变任意一个列表会改变另一个列表
b=cubes[:]

#例3：建立函数将字符串中的每一个单词作为一个元素保存到列表中
def words_list():
    message='The frist three items in the list are'
    a=[]
    char=''
    for words in message:
        #未遍历到空字符时合成字符形成字符串
        if words!=' ':
            char+=words
            #遍历到最后一个字符时，保存最后一个字符串加入列表
            if words==message[-1]:
                a.append(char)
        #遍历空格符保存前面相加形成的字符串加入列表
        else:
            a.append(char)
            #保存一个单词后清空char()
            char=''
    print(a)


