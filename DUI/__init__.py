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
import time

def __version__():
	return "1.0.1"

def test1():
	print("测试按钮1被点击")
	time.sleep(1)
def test2():
	print("测试按钮2被点击")
	time.sleep(1)
def test3():
	print("测试按钮3被点击")
	time.sleep(1)

def showTestWindow():
	f = Frame()

	mainWindow = Window("主界面")
	mainWindow.addWidget(2, Text("DUI库的测试窗口", 0))
	mainWindow.addWidget(4, Text("版本:V0.1.0", 1))
	mainWindow.addWidget(6, Text("作者:Lettle", 1))
	mainWindow.addWidget(8, Text("w向上s向下y确认", 1))
	mainWindow.addWidget(8, Text("一起学习?加作者QQ:1071445082", 1))
	mainWindow.addWidget(10, Text("---By Lettle", 2))
	mainWindow.addWidget(11, Button("测试按钮1", onClick=test1))
	mainWindow.addWidget(12, Button("测试按钮2", onClick=test2))
	mainWindow.addWidget(13, Button("测试按钮3", onClick=test3))
	mainWindow.addWidget(14, Button("退出(点击或输入quit)", onClick=quit))
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
