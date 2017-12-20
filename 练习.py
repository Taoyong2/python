# coding:utf-8
# author: Tao yong
# Python

'''
    例：建立函数fizzbuzz，遍历1到n的所有整数，当能被3整除时打印fizz
    当能被5整除时打印buzz，同时能被3和5整除时打印fizzbuzz，都不能整除时返回该整数的字符
'''

def fizzbuzz(n):
    a=[]
    for n in range(1,n+1):
        if n%3==0:
            if n%5==0:
                a.append('fizzbuzz')
            else:
                a.append('fizz')
        elif n%5==0:
            a.append('buzz')
        else:
            a.append(str(n))
    print(a)
fizzbuzz(15)
