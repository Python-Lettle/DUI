#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: *.py
from DUI.Widgets import Widget

class Text(Widget):
	def __init__(self, text="", type=0):
		super().__init__()
		super().setText(text,type)