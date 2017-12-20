# coding:utf-8
# author: Tao yong
# Python

'''
    可视化包pygal生成可缩放的矢量图形文件，在不同尺寸的屏幕上自动缩放
    最简单的方法是通过浏览器打开图表（谷歌浏览器快捷键Ctrl+O打开电脑文件
    生成条形图使用Bar（）函数
'''

from random import randint

class Die():
    '''表示一个骰子的类'''

    def __init__(self,num_sides=6):
        '''骰子默认为六面'''
        self.num_sides=num_sides

    def roll(self):
        '''返回一个位于1和骰子面数之间的随机数'''
        return randint(1,self.num_sides)
