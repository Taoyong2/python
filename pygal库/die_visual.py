# coding:utf-8
# author: Tao yong
# Python

from die import Die
import pygal

#创建两个骰子对象
die_1 =Die()
die_2 =Die(10)

#掷几次骰子，并将结果存在一个列表里
results=[]
for roll_num in range(50000):
    result=die_1.roll()+die_2.roll()
    results.append(result)

#分析结果，每个数被掷到的次数
frequencies=[]
for value in range(1,die_1.num_sides+die_2.num_sides+1):
    #列表的count方法，计算该元素在列表中出现了多少次
    frequency=results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
#创建条形图实例
hist=pygal.Bar()

hist.title="Results of rolling two D6 1000 times."
hist.x_labels=['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16',]
hist.x_title='Result'
hist.y_title='Frequency of Result'

hist.add('D6+D10',frequencies)
hist.render_to_file('die_visual.svg')


