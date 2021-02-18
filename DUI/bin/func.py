#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: func.py

def slen(value):
    """超级len命令,能将中文算成两个位置"""
    length =len(value)
    utf8_length =len(value.encode('utf-8'))
    length =(utf8_length -length)/2+length
    return int(length)
