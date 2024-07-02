"""
Create by NianXiaoLing on 2023/04/13

# 一、发送http请求，两种方式
# 1. urllib，- python自带
# 2. requests(推荐) - 需要引入
# - 2.1 安装步骤1： 启动pipenv shell
# - 2.2 安装步骤2： pipenv install requests -i https://pypi.tuna.tsinghua.edu.cn/simple
# - 2.3 安装步骤3： 查看安装情况 pip list

# 二、定义类
# 1. class定义继续object在py3上是没有区别的，py2上有区别-经典类与新式类的区别
# 2. 静态方法装饰器 @staticmethod 与 @classmethod ，推荐前后。后者更像是类对像。
# 2.1 静态方法的函数里没有 self参数
# 2.2 在py2里显示的继承object为新式类，不写object为经典类；但在py3里所有的类都是新式类
# 2.3 新式类比经典类多很多优势，目前主流的版本都是新式类

"""
__author__ = "carmen"
'''
静态方法
 @staticmethod: 纯粹的静态方法
 @classmethod: 类的方法，如果用到类里面的属性或变量，推荐这种方式
 
'''

import requests

# scrap , request + beautiful soap


# 爬虫框架：多线程爬虫 scrapy
# 爬虫经典组合： request + beautiful soap
# 爬虫入门： https://zhuanlan.zhihu.com/p/30242648
# in python3 ：都是新式类 >> class HTTP(object) = class HTTP:
# in python2里有区别，存在经典类与新式类的区别, 前者为 新式类，后者为经典类
class HTTP:
    # 静态方法
    @staticmethod
    def GET(url, return_json=True):
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

    # 2. post方法
    def post(self):
        pass
