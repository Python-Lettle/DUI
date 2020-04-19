#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Lettle"
# QQ: 1071445082
# fileName: Widget.py
from DUI.bin.func import *


class Widget:
    def __init__(self, text="", type=0):
        self.text = text
        # 0 左对齐 1 居中 2 右对齐
        self.type = type
        # 0 Windows 1 Linux
        self.system = 0

    def setText(self, text, type=0):
        self.text = text
        self.type = type

    def getText(self, width, system):
        if system == 0:
            long = width
            b = 2
            textLength = slen(self.text)
        else:
            long = width
            textLength = slen(self.text)
            b = 0

        if self.type == 0:
            '''左对齐'''
            return self.text + " " * (long - textLength - b)
        elif self.type == 1:
            '''居中'''
            a = int((long - textLength - b)/2)
            return " "*a + self.text + " "*(long-a-textLength-2)
        else:
            '''右对齐'''
            return " " * (long - textLength -2) + self.text
