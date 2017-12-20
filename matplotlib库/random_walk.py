# coding:utf-8
# author: Tao yong
# Python

import matplotlib.pyplot as plt
from random import choice
#random模块 choice函数：在列表中随机选择一个元素返回

'''
    创建类RandomWalk()模拟随机漫步，三个变量
        1.存储随机漫步次数的变量
        2.存储随机漫步经过的x坐标
        3.存储随机漫步经过的y坐标
    两个方法
        1.__init__()
        2.fill_walk()
'''
class RandomWalk():
    '''一个生成随机漫步数据的类'''

    def __init__(self,num_points=5000):
        '''初始化随机漫步的属性'''
        self.num_points=num_points

        #所有随机漫步都始于（0,0）
        self.x_values=[0]
        self.y_values=[0]

    def fill_walk(self):
        '''计算随机漫步包含的所有点'''

        #不断漫步，直到列表到达指定的长度
        while len(self.x_values)<self.num_points:

            #决定前进方向以及沿着这个方向前进的距离(随机）
            x_direction=choice([1,-1])
            x_distance=choice([0,1,2,3,4])
            x_step=x_direction*x_distance

            y_direction=choice([1,-1])
            y_distance=choice([0,1,2,3,4])
            y_step=y_direction*y_distance

            #拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            #计算下一个点的x和y值(位置列表最后一个值加步长)
            next_x=self.x_values[-1]+x_step
            next_y=self.y_values[-1]+y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)



