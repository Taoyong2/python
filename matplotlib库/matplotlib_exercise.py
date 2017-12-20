# coding:utf-8
# author: Tao yong
# Python

'''
    matplotlib是一个第三方数学绘图库
    模块pyplot包含了很多生成图标的函数
    plot（）----折线图
    sctter（）----散点图
'''

from matplotlib库.random_walk import RandomWalk

#添加中文字体
from pylab import *
# 添加中文字体
from pylab import *

from matplotlib库.random_walk import RandomWalk

mpl.rcParams['font.sans-serif'] = ['SimHei']

#利用plot函数绘制简单的折线图
#修改plot函数默认参数linewidth
#默认plot函数x轴的点是0,1,2,3,4，……，square表示g各x值对应的y值
input_value=[1,2,3,4,5]
#设置各点的x轴坐标
squares=[1,4,9,16,25]
#设置各点的y轴坐标
plt.plot(input_value,squares,linewidth=5)

#设置图表标题，给x，y轴加上标签
plt.title('Square Numbers',fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel('Square of Value',fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',labelsize=14)

plt.show()


#使用sctter()函数绘制散点图
# x_values=[1,2,3,4,5]
# y_values=[1,4,9,16,25]

#利用循环代替计算绘制1000个点的图，y=x^2
x_values=list(range(0,1000))
y_values=[x**2 for x in x_values]

#散点默认蓝色点和黑色轮廓，edgecolor实参可改变轮廓，none删除数据点轮廓
#参数c可改变数据点颜色,可指定颜色，例：c='red'，也可以rgb模式(红，绿，蓝)自定义。例：c=(0,0,0.8)
#参数c的颜色映射，可根据函数实现颜色渐变，数值越小，颜色越浅，数值越大，颜色越深
plt.scatter(x_values,y_values,c=y_values,edgecolors='none',s=40)

#设置图表标题并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()

#例1：绘制前五个整数立方值的图形函数
def cube_5():
    x_values=list(range(0,5))
    y_values=[x**3 for x in x_values]

    plt.scatter(x_values,y_values,s=40)
    plt.title('前五个整数的立方值',fontsize=25)
    plt.xlabel('整数',fontsize=14)
    plt.ylabel('整数的立方值',fontsize=14)
    plt.tick_params(axis='both',which='major',labelsize=14)
    plt.show()

def cube_5000():
    x_values=list(range(0,5000))
    y_values=[x**3 for x in x_values]

    plt.scatter(x_values,y_values,s=40)
    plt.title('前五千个整数的立方值',fontsize=25)
    plt.xlabel('整数',fontsize=14)
    plt.ylabel('整数的立方值',fontsize=14)
    plt.tick_params(axis='both',which='major',labelsize=14)
    plt.show()

rw=RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values,rw.y_values,s=15)
plt.show()
