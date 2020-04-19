#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: Window.py

import os
from DUI.bin.func import *

# defaultSkin4Windows = [
#     "┌─┐",
#     "│┼│",
#     "└─┘"
# ]
defaultSkin4Windows = [
    "+-+",
    "|┼|",
    "+-+"
]

class SkinMaker:
    def __init__(self,skin):
        self.LeftUp = skin[0][0]
        self.RightUp = skin[0][2]
        self.LeftDown = skin[2][0]
        self.RightDown = skin[2][2]
        self.HorizontalLine = skin[0][1]
        self.VerticalLine = skin[1][0]
        self.corner = skin[1][1]

'''
    这是一个迭代器,使用它来迭代每一行要输出的屏幕内容
'''
class lineMaker:
    def __init__(self,title,width=30,height=20,system=0,skin=defaultSkin4Windows):
        self.title = title           # str
        self.width = width           # int
        self.height = height         # int
        self.system = system         # int
        self.skin = SkinMaker(skin)  # 是一个皮肤类型的class
        self.widgets = []            # 是一个包含多个tuple(line,widget)成员的List

    def __iter__(self):
        self.nowHeight = 1
        self.widget_temp = self.widgets.copy()
        return self

    def __next__(self):
        skin = self.skin
        widget_thisLine = None
        textThisLine = ""
        if self.nowHeight <= self.height:
            nowHeight = self.nowHeight
            self.nowHeight += 1
        else:
            '''如果迭代器超过了最后一位'''
            raise StopIteration

        if self.system == 0:
            blank = "  "
        elif self.system == 1:
            blank = " "

        if nowHeight != 1 and nowHeight != self.height:
            # 如果当前不是第一行或者最后一行
            # print(self.widget_temp)
            for widget in self.widget_temp:
                if widget[0] == nowHeight:         #如果控件是在这一行的
                    # 获得该行的控件
                    widget_thisLine = widget[1]     #将此控件取出
                    self.widget_temp.remove(widget)  #将此控件从缓存中删除
                    break
                else:
                    widget_thisLine = None
            if widget_thisLine:  #如果获取到了
                # 获得控件返回的文本
                textThisLine = widget_thisLine.getText(self.width, self.system)
            else:
                textThisLine = " " * (self.width - 2)
            # 组装窗口界面
            textThisLine = skin.VerticalLine + textThisLine + skin.VerticalLine

        elif nowHeight == 1:
            # 如果当前是第一行
            textThisLine = skin.LeftUp + skin.HorizontalLine + self.title + skin.HorizontalLine*(self.width - 5 - slen(self.title))+ "X"+ skin.HorizontalLine + skin.RightUp

        elif nowHeight == self.height:
            # 如果是最后一行
            textThisLine = skin.LeftDown + skin.HorizontalLine * (self.width - 2) + skin.RightDown

        return textThisLine

    def addWidgets(self,widget):
        self.widgets.append(widget)

    def setSystem(self, system):
        self.system = system

class Window:
    def __init__(self,title,width=30,height=20,system="Windows",skin=defaultSkin4Windows):
        self.lineMaker = lineMaker(title,width,height,system,skin)
    def addWidget(self,line,widget):
        widget.system = self.lineMaker.system
        self.lineMaker.addWidgets(tuple([line,widget]))

    def setSystem(self, system):
        self.lineMaker.setSystem(system)

    def showWindow(self):
        if self.lineMaker.system == 0:
            os.system("cls")
        else:
            os.system("clean")
        myiter = iter(self.lineMaker)
        for text in myiter:
            print(text)