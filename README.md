# DUI
## 简介

<br>它用print及一些基础库(sys,os等)制作，当你使用时不需要考虑太多兼容性问题,理论上能运行python解释器的地方就能使用,实际上我们经常会使用很多奇怪的终端界面（这个问题很难解决）
<br>
<br>但是你仍然可以用很少的代码获得一个比较美观的界面。
<br>此库尚未完善，只写了一点内容，以后会向更多功能进行制作。有兴趣的同学可联系我邮箱：1071445082@qq.com
<br>

DUI库可以通过

```shell
pip install DUI
```

 来实现安装库，如果要检查自己的DUI是否正常及其版本号，可以使用

```python
import DUI
DUI.showTestWindow()
```

来获取信息 。如果一切正常则会出现

```shell
+-主界面-------------------X-+
|DUI库的测试窗口              |
|                           |
|        版本:V0.1.0         |
|                           |
|        作者:Lettle         |
|                           |
|一起学习?加作者QQ:1071445082   |
|                            |
|                ---By Lettle|
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
+----------------------------+
```

这样的窗口（应该是对齐的）

## 标准DUI界面

### Frame

​	<br>Frame是界面的框架，用来写配置信息，如系统类型等。
    <br>Frame把Widget, Window, Listener, Controller, Alert集成在一起进行操作

#### Window

​	<br>Window是一个DUI界面最重要部分，它由开发者自行设计。一个DUI界面可以有多个Window且可以灵活地互相切换，由用户操作按钮来操控。
    <br>Window实际上可以单独使用,所有方法都是可以直接调用执行的,即脱离Frame单独显示
#### Listener

​	Listener是一个DUI界面用户操作部分监听工具，按钮、输入框等控件由Listener控制，最后返回给Frame。(此功能尚未完善)

#### Alert

​	Alert是一个DUI界面在Window下一行的提示语。(此功能尚未完善)

#### Widget

​	Widget为Window服务，可以调用Listener和Alert，最后组成一个开发者需要的组件。Widget为开发者提供基础的对象，开发者可以通过Widget对象扩展新的控件来充实自己的DUI界面。

​	DUI内置一个Text控件，继承自Widget类，开发者可以根据Text控件的写法来自行编写新的插件。