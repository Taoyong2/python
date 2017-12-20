# coding:utf-8
# author: Tao yong
# Python

from pygal_maps_world import i18n
from pygal_maps_world.i18n import SOUTH_AMERICA,NORTH_AMERICA
from pygal_maps_world import i18n
import pygal
wm=pygal.maps.world.World()
wm.title='North,central,and South America'

wm.add('North America',['ca','mx','us'])
wm.add('Center America',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South Amercia',['ar','bo','br','cl','co','ec','gf','gy','pe','py','sr','uy','ve'])

wm.rander_to_file('americas.svg')
