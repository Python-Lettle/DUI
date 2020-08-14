#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: Frame.py

from DUI.Frames.Listener import *

class Frame:
    def __init__(self,system="Windows"):
        self.windows = []  #储存window
        self.alert = None
        self.listener = Listener(0)

        #判断显示格式
        s = system.lower()
        if s == "windows" or s == "win" or s == "w":
            self.system = 0
        elif s == "linux" or s == "l":
            self.system = 1

    '''
        设置窗口皮肤
    '''
    def setSkin(self,skinList):
        self.skin = skinList

    '''
        传入一个自定义的Listener
    '''
    def setListener(self, listener):
        self.listener = listener

    '''
        添加新的窗口
    '''
    def addWindow(self,window,index):
        try:
            self.windows[index] = window
        except:
            self.windows.append(window)
            index = self.windows.__len__()-1
        self.windows[index].setSystem(self.system)

    def delWindow(self,index):
        del self.windows[index]

    '''
        调用窗口的显示方法来切换窗口
    '''
    def showWindow(self,index):
        self.windows[index].showWindow()
        while True:
            self.listener.run()
            self.windows[index].showWindow()