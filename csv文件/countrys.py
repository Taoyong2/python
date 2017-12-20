# coding:utf-8
# author: Tao yong
# Python

from pygal_maps_world.i18n import COUNTRIES

for country_code in sorted(COUNTRIES.key()):
        print(country_code,COUNTRIES[country_code])
