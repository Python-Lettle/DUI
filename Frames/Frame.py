#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: *.py

class Frame:
    def __init__(self,system="Windows"):
        self.windows = []

        s = system.lower()
        if s == "windows" or s == "win" or s == "w":
            self.system = 0
        elif s == "linux" or s == "l":
            self.system = 1

    def __del__(self):
        # print("Frame关闭")
        pass

    def setSkin(self,skinList):
        self.skin = skinList

    def addWindow(self,window,index):
        try:
            self.windows[index] = window
        except:
            self.windows.append(window)
            index = self.windows.__len__()-1
        self.windows[index].setSystem(self.system)

        # print("{}号窗口已经加载".format(index))

    def testMessage(self):
        print("成功导入此Frame!")

    def showWindow(self,index):
        self.windows[index].showWindow()