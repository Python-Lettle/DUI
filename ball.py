#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: ball.py

import time, os
from DUI import *
#DUI 加载
f = Frame(showFPS=True)
mainWindow = Window("弹球", width=34, height=16)
f.addWindow(mainWindow, 0)
for i in range(1,16):
	mainWindow.addWidget(i,Text())

height = 15
width = 15
map_01 = [['0' for i in range(height + 1)] for o in range(width + 1)]

ob_1 = {
	'x': 1,
	'y': 1,
	'k': 2,
	'ff': 0,
}


def update():
	if ob_1['ff'] == 0:
		ob_1['y'] = round(ob_1['k'] * (ob_1['x'] + 1 - ob_1['x']) + ob_1['y'])
		ob_1['x'] = ob_1['x'] + 1
		if (ob_1['x'] >= width):
			ob_1['x'] = width
			ob_1['ff'] = 1
			ob_1['k'] = ob_1['k'] * -1

		if (ob_1['y'] >= height):
			ob_1['y'] = height
			ob_1['k'] = ob_1['k'] * -1

		if (ob_1['y'] <= 0):
			# ob_1['y']=0
			ob_1['k'] = ob_1['k'] * -1

	if ob_1['ff'] == 1:
		ob_1['y'] = round(ob_1['k'] * (ob_1['x'] - 1 - ob_1['x']) + ob_1['y'])
		ob_1['x'] = ob_1['x'] - 1
		if (ob_1['x'] <= 0):
			ob_1['x'] = 0
			ob_1['ff'] = 0
			ob_1['k'] = ob_1['k'] * -1

		if (ob_1['y'] >= height):
			ob_1['y'] = height
			ob_1['k'] = ob_1['k'] * -1

		if (ob_1['y'] <= 0):
			ob_1['y'] = 0
			ob_1['k'] = ob_1['k'] * -1


def render():
	map_01[ob_1['x']][ob_1['y']] = "●"


def view():
	ii=1
	for i in map_01:
		txt = "".join(i).replace('0', "○")
		mainWindow.updateWidget(ii,Text(txt))
		ii += 1
	f.showWindow(0)



def renew():
	return [['0' for i in range(height + 1)] for o in range(width + 1)]


def main():
	time.sleep(0.3)
	update()
	#print(ob_1['x'], ob_1['y'])
	render()
	view()

for i in range(10000):
	map_01 = renew()
	main()
