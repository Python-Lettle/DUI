from DUI import Frame
from DUI import Window
t = Frame()
main_w = Window('主窗口',0)
main_w.add_widget('TextLine',3,way='C',text='DUI测试界面',wi_id='title')
main_w.add_widget('line',4,wi_id='line')
main_w.add_widget('TextLine',5,text='你可以用w向上s向下,y键确认,q键退出',wi_id='tishi')
main_w.add_widget('Button',6,text='测试按钮1',cursor_index=0,onclick_sen=r"print('1号成功')",wi_id='first')
main_w.add_widget('Button',7,text='测试按钮2',cursor_index=1,onclick_sen=r"print('2号成功')",wi_id='second')
main_w.add_widget('Button',8,text='测试按钮3',cursor_index=2,onclick_sen=r"print('3号成功')",wi_id='third')
t.add_window(main_w)
t.build(0)
t.listen(0,confirm="y",kill="q")
