#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Lettle"
# QQ: 1071445082
# fileName: test.py
import sys
sys.path.append("..")

'''
	从此处开始是程序主体
'''
import DUI
f = DUI.Frame("w")
mainWindow = DUI.Window("主界面")

text1 = DUI.Text("林雨辰的那只神经喵喵",0)
text2 = DUI.Text("Reder",1)
text3 = DUI.Text("AIVC[潜水数电中]",2)

mainWindow.addWidget(2, text1)
mainWindow.addWidget(4, text2)
mainWindow.addWidget(6, text3)

f.addWindow(mainWindow, 0)
f.showWindow(0)
