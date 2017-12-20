# coding:utf-8
# author: Tao yong
# Python

'''
    可视化前三个项目，并自定义添加工具提示
'''
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

my_style=LS(color='#333366',base_style=LCS)
chart=pygal.Bar(style=my_style,x_label_rotation=45,show_legend=False)

chart.title='Python Projects'
chart.x_labels=['httpie','django','flask']

#字典内含有两个键值对，pygal根据与键’value'相关联的数字确定条形的高度
#键‘label'对应的值为自定义提示
plot_dicts=[
    {'value':16101,'label':'Description of httpie'},
    {'value':15028,'label':'Description of django'},
    {'value':14798,'label':'Description of flask'},
]

chart.add('',plot_dicts)
chart.render_to_file('bar_descriptions.svg')
