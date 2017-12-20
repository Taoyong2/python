# coding:utf-8
# author: Tao yong
# Python

#字典是一系列键值对,用大括号表示
alien_0={}
alien_0={'points':5,'color':'green'}
#在字典的方括号中放入键，就可以访问该键对应的值
print(alien_0['points'])
new_points=alien_0['points']
print(3+new_points)
#添加键值对：字典[键]=值
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
#修改字典中的值
alien_0['color']='yellow'
print(alien_0)
#删除字典里的值
del alien_0['color']
print(alien_0)

#遍历字典中所有键值对
user_0={
    'username':'efermi',
    'frist':'enrico',
    'last':'fermi',
}
#item()方法返回一个键—值对，列表返回顺序与存储顺序不同
for key,value in user_0.items():
    print('\nkey:'+key+'\nvalue:'+value)
#遍历字典中的所有键
#key()方法返回字典中的键，获取顺序不可预测
for key in user_0.keys():
    print('\nkey:'+key)
# sorted函获得按特定顺序排列的键列表
#value()方法返回字典中的值，获取顺序不可预测
for value in sorted(user_0.values()):
    print('\nvalue:'+value)
#set()方法剔除重复项
for value in set(user_0.values()):
    print('\nvalue:'+value)

#字典的嵌套，将字典作为列表的值存储在字典中
alien_1={'color':'green','points':5}
alien_2={'color':'yellow','points':10}
alien_3={'color':'red','points':15}
aliens=[alien_1,alien_2,alien_3]
for alien in aliens:
    print(alien)

#当字典的键想关联多值时，可以在字典中嵌套一个列表
#字典也可以嵌套字典

#input函数接受用户输入，input函数内的内容表示输出提示用户输入的内容
#input接受字符串变量输出
'''
    message=input('please input your name:')
    print('The user name is:'+message)
'''
#input默认接受字符串内容，若想输入整数，需用int()函数进行类型转换
'''
    age=int(input('how old are you?'))
    if age>=18:
        print('yes')
    else:
        print('no')
'''

#while循环,满足条件循环，不满足条件跳出循环
#避免无限循环，ctrl+c无限循环时关闭程序输出的终端窗口
current_number=1
while current_number<=5:
    print(current_number)
    current_number+=1

#while True可不断循环，直至break语句跳出循环,break语句跳出整个循环
'''
    while True:
    city=input("please enter the name of a city you have visited(Enter 'quit'quit):")
    if city=='quit':
        break
    else:
        print("I'd love to go to "+city.title()+'!')
'''

#continue语句，跳出当前循环，执行下一次循环

#while循环处理列表和字典
#1.在列表之间移动元素
#2.删除列表中的特定值
    #删除列表中的‘cat'元素
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)
#使用用户输入来填充字典
