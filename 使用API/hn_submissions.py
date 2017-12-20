# coding:utf-8
# author: Tao yong
# Python

'''
    执行一个API调用，返回Hacker News上当前热门文章的Id，
    再查看每篇排名靠前的文章
'''

import pygal
import requests
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

url='https://hacker-news.firebaseio.com/v0/topstories.json'

r=requests.get(url)

print('Status code',r.status_code)
