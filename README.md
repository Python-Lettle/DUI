# DUI
## 简介

<br>它用print及一些基础库(sys,os,re等)制作，当你使用时不需要考虑太多兼容性问题（这个问题很难解决），你就可以获得一个比较美观的界面。
<br>此库尚未完善，只写了一点内容，以后会向更多功能进行制作。有兴趣的同学可联系我邮箱：1071445082@qq.com
<br>文件注释:终端下运行命令```python example.py```可直接欣赏此库的样例作品。
<br>运行```python DUI-V0.2.py```也可以看到相同样例。DUI.py为直接调用的库文件,不内置样例。如果想使用DUI库须将DUI.py文件及其所需的getchar.so文件复制到您的项目中然后即可调用此库。
<br>**在termux环境下直接运行原版将会报错**，需要将termux版的getchar.so替换根目录下的getchar.so
<br>暂不支持setup.py



## 标准DUI界面

### Frame

​	Frame是界面的框架，用来写配置信息，如系统类型等。

#### Window

​	Window是一个DUI界面最重要部分，它由开发者自行设计。一个DUI界面可以有多个Window且可以灵活地互相切换，由用户操作按钮来操控。

#### Listener

​	Listener是一个DUI界面用户操作部分监听工具，按钮、输入框等控件由Listener控制，最后返回给Frame。(此功能尚未完善)

#### Alert

​	Alert是一个DUI界面在Window下一行的提示语。(此功能尚未完善)

#### Widget

​	Widget为Window服务，可以调用Listener和Alert，最后组成一个开发者需要的组件。Widget为开发者提供基础的对象，开发者可以通过Widget对象扩展新的控件来充实自己的DUI界面。

​	DUI内置一个Text控件，继承自Widget类。