# coding:utf-8
# author: Tao yong
# Python

#导入json模块，加载json文件数据
import json

#将数据加载到一个列表里
filename='population_data.json'
with open(filename) as f:
    pop_data=json.load(f)

#打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year']=='2010':
        country_name=pop_dict['Country Name']
        #有些数据含有小数，int不能将含有小数的字符串转换整数
        #需要先转换成浮点数，在转换成整数，舍弃小数部分
        population=int(float(pop_dict['Value']))
        print(country_name+':'+str(population))
