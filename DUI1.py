#-*-coding:utf-8;-*-
#python3
#author:Lettle
import os,sys
#控件库------------------------------------------------------------------------------
class Line():
    def __init__(self,name,location):
        self.name = name
        self.location = location

#主框架------------------------------------------------------------------------------
class TestUIFrame():
    def __init__(self):
        self.sys = "Windows"
        self.height = 10
        self.width = 10
        self.widget = []
        self.dict = {"line":1,"input":2}
    def set_sys(self,sys):
        self.sys = sys
    def set_size(self,height,width):
        self.height = int(height)
        self.width = int(width)
    def add_widget(self,widget_name,widget_location):
        for i in range(1):        #更新控件库记得修改这里------------------------------
            if widget_name == "line":
                widget = Line(widget_name,widget_location)
        self.widget.append(widget)
    def build(self):
        if self.sys == "Windows":  #判断系统进行清屏
            os.system("cls")
        else:
            os.system("clear")
        def build_fbte(i):        #fbte:From begining to end
            if i == 0:
                print("╔"+"═"*(self.width-2)+"╗")
                return False
            elif i == self.height-1:
                print("╚"+"═"*(self.width-2)+"╝")
                return False
            else:
                return True

        if len(self.widget) == 0:        #判断有无控件
            for i in range(self.height):
                if build_fbte(i):
                    print("║"+"  "*(self.width-2)+"║")
        else:
            widget_a = len(self.widget)
            widget_task = self.widget
            for i in range(self.height):
                if build_fbte(i):
                    for ii in range(widget_a):
                        if widget_task[ii].location == i:
                            print("╠"+"═"*(self.width-2)+"╣")
                        else:
                            print("║"+"  "*(self.width-2)+"║")
            
if __name__=="__main__":
    t = TestUIFrame()
    t.set_sys("Windows")
    t.set_size(20,20)
    t.add_widget("line",10)
    t.add_widget("line",15)
    t.add_widget("line",17)
    t.build()
