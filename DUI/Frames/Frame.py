#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: Frame.py

from DUI.Frames.Listener import *
import time

class Frame:
    def __init__(self,system="Windows",showFPS=False,noClean=False):
        self.windows = []  #储存window
        self.alert = None
        self.listener = Listener(0)
        self.nowWindow = None
        self.showFPS = showFPS
        self.noClean = noClean
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
    def updateWindow(self, window, index):
        self.windows[index] = window
    def delWindow(self,index):
        del self.windows[index]

    '''
        调用窗口的显示方法来切换窗口
    '''
    def showWindow(self,index):
        if self.showFPS:
            time_start = time.time()  # 开始计时

        win = self.windows[index]
        win.showWindow(noClean=self.noClean)
        self.nowWindow = index
        pointButton = win.getPointButton()
        if pointButton != None:
            self.listener.setPointButton(pointButton)

        if self.showFPS:
            time_end = time.time()  # 结束计时
            FPS = 1/(time_end - time_start)
            print("FPS:",int(FPS))