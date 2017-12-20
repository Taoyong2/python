# coding:utf-8
# author: Tao yong
# Python

'''
    模拟多次随机漫步
'''
import matplotlib.pyplot as plt

from matplotlib库.random_walk import RandomWalk

#当用户输入y时会重新进行一次随机漫步
while True:
    #创建rw对象，使用fill_walk()方法
    rw=RandomWalk()
    rw.fill_walk()

    #设置绘图窗口的尺寸
    plt.figure(dpi=128,figsize=(10,6))

    #浅蓝到深蓝的颜色映射
    point_color=list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_color,cmap=plt.cm.Blues,edgecolors='none',s=1)

    #重绘起点和终点
    plt.scatter(0,0,c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    no_running=0
    while True:
        #向用户确认是否进行下一次随机漫步
        keep_running=input("\nMake another walk?(y/n)")
        #n表示不进行，利用变量no_running跳出两层循环，程序结束
        if keep_running=='n':
            no_running+=1
            break
        #y表示进行，跳出内层循环，重新执行外层循环，进行下一次随机漫步
        elif keep_running=='y':
            break
        #用户输入错误，提示用户重新输入，重新执行内层循环
        else:
            print('Please input again')
            continue
    #利用变量no_running判断是否进行下一次随机漫步
    if no_running==1:
        break
