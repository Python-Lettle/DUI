#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: *.py

def singleton(cls):
    _instance = {}#使用不可变的类地址作为键，其实例作为值，每次创造实例时，
               #首先查看该类是否存在实例，存在的话直接返回该实例即可，
               #否则新建一个实例并存放在字典中。

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner

def slen(value):
    """超级len命令,能将中文算成两个位置"""
    length =len(value)
    utf8_length =len(value.encode('utf-8'))
    length =(utf8_length -length)/2+length
    return int(length)