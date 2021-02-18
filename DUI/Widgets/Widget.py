#!/usr/bin/env python
# -*- coding:utf-8 -*-
# __author__ = "Lettle"
# QQ: 1071445082
# fileName: Widget.py

class Widget:
    def __init__(self, widget_type, id=None):
        #标注控件类型
        self.widget_type = widget_type
        self.id = id

    def getType(self):
        return self.widget_type
    def setType(self, type):
        self.widget_type = type
    def getId(self):
        return self.id
    def setId(self, id):
        self.id = id