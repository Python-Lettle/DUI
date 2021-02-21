#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: Canvas.py
from DUI.Widgets.Widget import *
from DUI.Widgets.Text import *

class Canvas(Widget):
	def __init__(self, content=None, height=0, line=1):
		super().__init__("Canvas")
		if content is None:
			content = []
		self.height = height
		self.line = line
		self.content = content

	def setContent(self, content):
		# 传入的Content目前只能是list
		self.content = content
		return self

	def setCanvas(self, window):
		# 在 window.addWidget时触发
		for i in range(self.height):
			window.addWidget(self.line+i, Text())
		return window

	def showCanvas(self, window):
		if self.content:
			for i in range(self.height):
				window.updateWidget(self.line+i, Text(self.content[i]))
		return window