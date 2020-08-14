#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Lettle"
# QQ: 1071445082
# fileName: Widget.py

class Widget:
    def __init__(self, widget_type):
        #标注控件类型
        self.widget_type = widget_type

    def getType(self):
        return self.widget_type
    def setType(self, type):
        self.widget_type = type