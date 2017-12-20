# coding:utf-8
# author: Tao yong
# Python

from pygal_maps_world.i18n import COUNTRIES
#字典Countries中包含国家名和对应国别码(两个字母)，pygal使用两个字母的国别码

def get_country_code(country_name):
    '''根据国家名，返回两个字母的国别码的函数'''
    for code,name in  COUNTRIES.items():
        if name == country_name:
            return code
    #如果没有找到指定的国家，就返回None
    return None
