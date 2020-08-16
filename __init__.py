# -*- coding:utf-8 -*-
# @Time    : 2020-4-14
# @Author  : Lettle

'''
	引入所有DUI重要组成部分
	Frames
	|  Alert.py
	|  Frame.py
	|  Listener.py
	|  Window.py
	Widgets
	|  Button.py
	|  Text.py
	|  Widget.py   (父类)
'''
from DUI.Frames import *
from DUI.Widgets import *
from DUI.bin import *
from random import randint

def __version__():
	return "1.0.1"

def showTestWindow():
	f = Frame("w")  # 参数 "w" 代表Windows系统格式

	mainWindow = Window("主界面")
	mainWindow.addWidget(2, Text("DUI库的测试窗口", 0))
	mainWindow.addWidget(4, Text("版本:V0.1.0", 1))
	mainWindow.addWidget(6, Text("作者:Lettle", 1))
	mainWindow.addWidget(8, Text("一起学习?加作者QQ:1071445082", 1))
	mainWindow.addWidget(10, Text("---By Lettle", 2))

	mainWindow.addWidget(11, Button("测试按钮1"))
	mainWindow.addWidget(12, Button("测试按钮2"))
	mainWindow.addWidget(13, Button("测试按钮3"))

	f.addWindow(mainWindow, 0)

	dict = \
		{
			"quit": quit,
			"w": mainWindow.up,
			"s": mainWindow.down,
			"y": mainWindow.confirm
		}
	listen = Listener(0)
	listen.setDict(dict)
	f.setListener(listen)

	while True:
		f.showWindow(0)
		f.listener.run()
