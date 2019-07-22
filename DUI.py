#-*-coding:utf8;-*-
#python3

__author__='Lettle'
import os,sys,re

from bin.widget import *


#Main framework
class Frame():
    def __init__(self):
        self.windows = []
        self.Listener = Listener(False)
        self.cursor = 0
        self.Button_num = 0
    def add_window(self,wd):
        self.windows.append(wd)
    def listen(self,mark_=0,confirm="y",kill="q"):
        self.Listener.running = True
        self.Listener.run(self,mark=mark_,confirm_key=confirm,kill_key=kill)
    def build(self,mark=0):
        self.windows[mark].buildW(self)

