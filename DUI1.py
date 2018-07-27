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
                widget = Line(widget_name,widget_location-1)
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
        widget_a = len(self.widget)
        if widget_a == 0:        #判断有无控件
            for i in range(self.height):
                if build_fbte(i):
                    print("║"+"  "*(self.width-2)+"║")
        else:
            widget_task = self.widget
            a = 0
            for i in range(self.height):
                if build_fbte(i):
                    if widget_a != 0:
                        for ii in range(widget_a):
                            if widget_task[ii].location == i:    #查询当前控件任务的位置
                                print("╠"+"═"*(self.width-2)+"╣")
                                del widget_task[ii]
                                widget_a = len(widget_task)
                                a = 1
                                break
                        if a != 1:
                            print("║"+"  "*(self.width-2)+"║")
                        a = 0
                    else:
                        print("║"+"  "*(self.width-2)+"║")
if __name__=="__main__":
    t = TestUIFrame()
    t.set_sys("Windows")
    t.set_size(20,20)
    t.add_widget("line",3)
    t.add_widget("line",4)
    t.add_widget("line",5)
    t.add_widget("line",6)
    t.add_widget("line",7)
    t.add_widget("line",9)
    t.add_widget("line",11)
    t.add_widget("line",13)
    t.add_widget("line",15)
    t.build()
