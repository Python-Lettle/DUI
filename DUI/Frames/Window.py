#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: Window.py
import os

from DUI.bin import *

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
#皮肤构造器
class SkinMaker:
    def __init__(self,skin):
        self.LeftUp = skin[0][0]
        self.RightUp = skin[0][2]
        self.LeftDown = skin[2][0]
        self.RightDown = skin[2][2]
        self.HorizontalLine = skin[0][1]
        self.VerticalLine = skin[1][0]
        self.corner = skin[1][1]

#控件管理器
class Widgeter:
    def __init__(self):
        self.widgets = []
        self.alerts = []
        self.canvas = []

    def append(self, widget):
        if widget[1].getType() == "Alert":
            self.alerts.append(widget)
        elif widget[1].getType() == "Canvas":
            self.canvas.append(widget)
        else:
            self.widgets.append(widget)
    def get(self, index):
        if index:
            return self.widgets[index]
        else:
            return None
    def update(self, widgetTuple):
        i = 0  # 计数器

        # 如果是Alert
        if widgetTuple[1].getType() == "Alert":
            for w in self.alerts:
                if w[0] == widgetTuple[0]:
                    # 如果Alert的id和当前控件相同
                    self.alerts[i] = widgetTuple
            i += 1

        # 如果是其他控件
        for w in self.widgets:
            if w[0] == widgetTuple[0]:
                # 如果控件的行数和当前控件相同
                self.widgets[i] = widgetTuple
            i += 1

    def getList(self):
        return self.widgets

#这是一个迭代器,使用它来迭代每一行要输出的屏幕内容
class LineMaker:
    def __init__(self, title, width=30, height=20, system=0, skin=None):
        if skin is None:
            skin = defaultSkin4Windows
        self.title = title           # str
        self.width = width           # int
        self.height = height         # int
        self.system = system         # int
        self.skin = SkinMaker(skin)  # 是一个皮肤类型的class
        self.widgeter = Widgeter()   # 是一个包含多个tuple(line,widget)成员的List

    def __iter__(self):
        self.nowHeight = 1
        self.widget_temp = self.widgeter.widgets.copy()
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

        #开始绘制Widget
        if nowHeight != 1 and nowHeight != self.height:
            # 如果当前不是第一行或者最后一行
            for widget in self.widget_temp:
                if widget[0] == nowHeight:         #如果控件是在这一行的
                    # 获得该行的控件
                    widget_thisLine = widget[1]     #将此控件取出
                    self.widget_temp.remove(widget)  #将此控件从缓存中删除
                    break
                else:
                    widget_thisLine = None
            if widget_thisLine:  #如果获取到了
                if widget_thisLine.getType == "Button":
                    pass
                else:
                    # 获得控件返回的文本
                    textThisLine = widget_thisLine.print(self.width, self.system)
            else:
                textThisLine = " " * (self.width - 2)
            # 组装窗口界面
            textThisLine = skin.VerticalLine + textThisLine + skin.VerticalLine

        elif nowHeight == 1:
            # 如果当前是第一行
            textThisLine = skin.LeftUp + skin.HorizontalLine + self.title + skin.HorizontalLine*(self.width - 5 - slen(self.title)) + "X" + skin.HorizontalLine + skin.RightUp

        elif nowHeight == self.height:
            # 如果是最后一行
            textThisLine = skin.LeftDown + skin.HorizontalLine * (self.width - 2) + skin.RightDown

        return textThisLine

    def addWidgets(self,widgetTuple):
        self.widgeter.append(widgetTuple)
    def updateWidget(self,widgetTuple):
        self.widgeter.update(widgetTuple)
    def getWidgets(self):
        return self.widgeter.getList()
    def getWidgeter(self):
        return self.widgeter
    def getWidget(self,index):
        return self.widgeter.widgets[index]
    def setSystem(self, system):
        self.system = system
    def setWindowIndex(self, windowIndex):
        self.windowIndex = windowIndex

class Window:
    def __init__(self, title, width=30, height=20, system=0, skin=None):
        if skin is None:
            skin = defaultSkin4Windows
        self.lineMaker = LineMaker(title,width,height,system,skin)  #渲染器对象   iter
        self.pointCondition = True
        self.buttonIndex = None           #按钮控件在 linemaker 中的位置

    def addWidget(self,line,widget):
        #添加一个控件
        if widget.getType() == "Button" and self.pointCondition:
            '''
                如果是按钮 则将指针指向按钮并且添加控件不再改变
            '''
            widget.pointed()
            self.pointCondition = None
            self.buttonIndex = len(self.lineMaker.getWidgets())
        elif widget.getType() == "Alert":
            widget.setWindowWidth(self.lineMaker.width)
            widget.setSkinMaker(self.lineMaker.skin)
        elif widget.getType() == "Canvas":
            self = widget.setCanvas(self)
        else:
            widget.system = self.lineMaker.system
        self.lineMaker.addWidgets(tuple([line,widget]))
        return self
    def updateWidget(self, line, widget):
        if widget.getType() == "Alert":
            widget.setWindowWidth(self.lineMaker.width)
            widget.setSkinMaker(self.lineMaker.skin)
        self.lineMaker.updateWidget(tuple([line,widget]))
        return self

    def setSystem(self, system):
        self.lineMaker.setSystem(system)
        return self
    def getPointButton(self):
        return self.lineMaker.getWidgeter().get(self.buttonIndex)
    '''
        页面指针控制
    '''
    def up(self):
        widgets = self.lineMaker.getWidgets()
        if len(widgets) != 0:
            for i in widgets[:self.buttonIndex]:
                if i[1].getType() == "Button":
                    #如果当前指针上面还有按钮
                    self.lineMaker.getWidgets()[self.buttonIndex][1].leave()
                    self.buttonIndex -= 1
                    self.lineMaker.getWidgets()[self.buttonIndex][1].pointed()
                    return
    def down(self):
        widgets = self.lineMaker.getWidgets()
        if len(widgets) != 0:
            for i in widgets[self.buttonIndex+1:]:
                if i[1].getType() == "Button":
                    #如果当前指针下面还有按钮
                    self.lineMaker.getWidgets()[self.buttonIndex][1].leave()
                    self.buttonIndex += 1
                    self.lineMaker.getWidgets()[self.buttonIndex][1].pointed()
                    return
    #按钮确认键
    def confirm(self):
        widgeter = self.lineMaker.getWidgeter()
        widgeter.get(self.buttonIndex)[1].press()

    '''
        显示窗口
    '''
    def showWindow(self, noClean=False):

        # 清屏
        if not noClean:
            if self.lineMaker.system == 0:
                os.system("cls")
            else:
                os.system("clear")

        #先导入Canvas
        for c in self.lineMaker.widgeter.canvas:
            self = c[1].showCanvas(self)

        #显示控件
        myiter = iter(self.lineMaker)
        for text in myiter: print(text)

        # 显示Alert
        for a in self.lineMaker.widgeter.alerts:
            a[1].showAlert()
        return self