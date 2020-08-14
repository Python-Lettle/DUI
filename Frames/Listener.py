#!/usr/bin/env python
# -*- coding:utf-8 -*-
#__author__ = "Lettle"
#QQ: 1071445082
#fileName: Listener.py

from DUI.Widgets import Widget

class Listener(Widget):
    def __init__(self, dict={}, mode=0):
        super().__init__("Listener")  #参数: 标明自身类型
        self.mode = mode     # 0 为原生input监听   1 为C扩展监听

        if dict == {}:
            dict = \
            {
                "w": print("up"),
                "s": print("down"),
                "a": print("left"),
                "d": print("right")
            }
        self.dict = dict
        '''当前指针行'''

    def setDict(self,dict):
        self.dict = dict

    def run(self):
        if self.mode == 0:
            res = input("->")  #按键结果
            for key, func in self.dict.items():
                if res == key:
                    func()

        return True