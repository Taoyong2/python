# coding:utf-8
# author: Tao yong
# Python

'''
    1.导入整个模块              import module_name
    2.导入模块中的函数          from module_name import function_name
    3.关键字as给函数指定别名    from module_name import function_name as fn
    4.as给模块指定别名          import module_name as mn
    5.导入模块中的所有函数      from module import *
'''

#类的继承
#子类ElectricCar继承父类car的所有功能，调用car的__init__方法
class car:
    pass
class ElectricCar(car):
    pass
'''
    1.导入模块中的类              from module import class
    2.一个模块可存放多个类，但最好存放某些具有关联性的类
    3.从一个模块中导入多个类      from module import class1,class2 
    4.导入整个模块                import module
    5.导入模块中的所有类          from module import *
    6.python标准库是一组默认安装的模块
    7.类名应采用驼峰命名法，每个单词首字母大写，不使用下划线
'''
