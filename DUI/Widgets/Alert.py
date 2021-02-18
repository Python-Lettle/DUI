#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: Alert.py
from DUI.Widgets import Widget
from DUI.Frames.Window import SkinMaker
from DUI.bin import *

class Alert(Widget):
    def __init__(self,text=""):
        super().__init__("Alert",None)
        self.text = text
        self.window_width = None
        self.skinmaker = None

    def setWindowWidth(self,width):
        #设置窗口宽度
        self.window_width = width
    def setSkinMaker(self,skin):
        self.skinmaker = skin

    def showAlert(self):
        if self.text != "":
            textLength = slen(self.text)
            textThisLine = self.text + " "*(self.window_width - textLength - 2)
            textThisLine = self.skinmaker.VerticalLine + textThisLine + self.skinmaker.VerticalLine
            print(textThisLine)
            print(self.skinmaker.HorizontalLine * self.window_width)