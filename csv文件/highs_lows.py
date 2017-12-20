# coding:utf-8
# author: Tao yong
# Python

#python 标准库中的csv模块，处理csv格式的文件
import csv

#datetime模块添加日期格式
from datetime import datetime

#读取csv文件后转化为可视化图表
from matplotlib import pyplot as plt

#分析文件头
#将文件名存储在filename中，打开结果文件并存储在fzhong
filename='death_valley_2014.csv'
with open(filename) as f:

    #调用csv模块的reader()函数将文件存储在阅读器对象中
    reader=csv.reader(f)

    #调用csv模块的next()函数返回文件的下一行，即第一行(文件头)
    header_row=next(reader)

    #获取reader从第二行开始的实际数据，存储在列表里
    dates,highs,lows=[],[],[]
    for row in reader:
        '''
            try-except-else代码块
            读取try内容时，若因为空行而导致ValueError，则执行except，告知错误missing
            否则执行else，读取正确数据
        '''
        try:
            #获取时间数据(第一列)，添加到列表dates中
            current_date=datetime.strptime(row[0],'%Y-%m-%d')

            #获取最高气温数据(第二列)，添加到列表highs中
            highs.append(int(row[1]))

            #获取最低气温数据(第四列)，添加到列表中
            lows.append(int(row[3]))
        except ValueError:
            print(current_date,'missing')
        else:
            dates.append(current_date)
    #创建窗口对象，设置窗口分辨率及长宽比
    fig =plt.figure(dpi=128,figsize=(10,6))

    #根据数据绘制图形，设置颜色,alpha参数代表颜色透明度
    plt.plot(dates,highs,c='red',alpha=0.5)
    plt.plot(dates,lows,c='blue',alpha=0.5)
    plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

    #设置图形的格式
    plt.title('Daily high temperatures - 2014',fontsize=24)
    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate()            #绘制斜的日期标签
    plt.ylabel('Temperature(F)',fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)

    plt.show()


