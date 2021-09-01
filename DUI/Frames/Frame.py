#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: Frame.py

from DUI.Frames.Listener import *
import time,os,platform

class Frame:
    def __init__(self,system=None,showFPS=False,noClean=False,canvasMode=None):
        self.windows = []  #储存window
        self.alert = None
        self.listener = Listener(0)
        self.nowWindow = None
        self.showFPS = showFPS
        self.noClean = noClean
        self.canvasMode = canvasMode
        #判断系统
        if system:
            s = system.lower()
        else:
            s = platform.system().lower()
        if s == "windows" or s == "win" or s == "w":
            self.system = 0
        elif s == "linux" or s == "l":
            self.system = 1


    def setSkin(self,skinList):
        '''
            设置窗口皮肤
        '''
        self.skin = skinList

    def setListener(self, listener):
        '''
            传入一个自定义的Listener
        '''
        self.listener = listener

    def addWindow(self,window,index):
        '''
            添加一个新的窗口
        '''

        try:
            self.windows[index] = window
        except:
            self.windows.append(window)
            index = self.windows.__len__()-1
        self.windows[index].setSystem(self.system)
        self.windows[index].setCanvasMode(self.canvasMode)

    def updateWindow(self, window, index):
        '''
            刷新窗口
        '''
        self.windows[index] = window

    def delWindow(self,index):
        '''
            删除一个窗口
        '''
        del self.windows[index]

    def showWindow(self,index):
        '''
            调用窗口的显示方法来切换窗口
        '''
        if self.showFPS:
            time_start = time.time()  # 开始计时
        if self.nowWindow != index:
            if self.system:
                os.system('clear')
            else:
                os.system('cls')

        win = self.windows[index]
        win.showWindow(noClean=self.noClean)
        
        self.nowWindow = index
        pointButton = win.getPointButton()
        if pointButton != None:
            self.listener.setPointButton(pointButton)

        if self.showFPS:
            time_end = time.time()  # 结束计时
            try:
                FPS = 1/(time_end - time_start)
            except ZeroDivisionError:
                FPS = 9999
            print("FPS:",int(FPS))

