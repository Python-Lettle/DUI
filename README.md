# DUI
## 简介

它用print及一些基础库(sys,os等)制作，当你使用时不需要考虑太多兼容性问题,理论上能运行python解释器的地方就能使用,实际上我们经常会使用很多奇怪的终端界面（这个问题很难解决）

但是你仍然可以用很少的代码获得一个比较美观的界面。
此库尚未完善，只写了一点内容，以后会向更多功能进行制作。有兴趣的同学可联系我邮箱：1071445082@qq.com

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
|DUI库的测试窗口             |
|                            |
|        版本:V0.1.0         |
|                            |
|        作者:Lettle         |
|                            |
|一起学习?加作者QQ:1071445082|
|                            |
|                ---By Lettle|
|>|测试按钮1                 |
|测试按钮2                   |
|测试按钮3                   |
|                            |
|                            |
|                            |
|                            |
|                            |
|                            |
+----------------------------+
->
```

这样的窗口（在Windows cmd中应该是对齐的）

更好的例子在项目中的guess.py中，直接运行

```
python guess.py
```

就可以体验DUI多窗口的乐趣了！

## 快速开始

首先，准备好`python, pip`环境

通过如下命令安装DUI库

```
pip install DUI
```

下面演示一个基本`DUI`界面的例子

```
from DUI import *
f = Frame("w")  # 参数"w"代表Windows格式,详细信息请查阅文档
mainWindow = Window("主界面") #参数为窗口标题,将写在上边框左侧
mainWindow.addWidget(2, DUI.Text("DUI库的测试窗口", 0))
f.addWindow(mainWindow, 0)
f.showWindow(0)
```

此时一个简单的带一行文字窗口创建成功！

## DUI文档

### Frame

Frame把Widget, Window, Listener, Alert集成在一起进行操作

Frame是界面的框架，`DUI`的一切动作将通过Frame来实现，比如`showWindow`

#### Frame()
|参数|类型|说明|默认值|
|:-:|:-:|:-:|:-:|
|system|`str`| 点击位置x坐标 |Windows|
获取一个Frame对象:

```python
from DUI import *
frame = Frame()
```

#### frame.addWindow()

> 添加窗口

|  参数  |  类型  |                 说明                 | 默认值 |
| :----: | :----: | :----------------------------------: | :----: |
| window | Window |             要传入的窗口             |        |
| index  | `int`  | 要传入的窗口的索引值**(按顺序加入)** |        |

#### frame.showWindow()

> 显示一个已经加载到Frame的窗口

| 参数  | 类型  |         说明         | 默认值 |
| :---: | :---: | :------------------: | :----: |
| index | `int` | 要显示的窗口的索引值 |        |

#### frame.updateWindow()

> 刷新一个窗口

|  参数  |  类型  |                  说明                  | 默认值 |
| :----: | :----: | :------------------------------------: | :----: |
| window | Window |              要刷新的窗口              |        |
| index  | `int`  | 要刷新的窗口的索引值**(按原位置填写)** |        |

#### frame.delWindow()

> 删除一个窗口

| 参数  | 类型  |         说明         | 默认值 |
| :---: | :---: | :------------------: | :----: |
| index | `int` | 要删除的窗口的索引值 |        |

#### frame.setListener()

> 传入监听器

|   参数   |    类型    |         说明         | 默认值 |
| :------: | :--------: | :------------------: | :----: |
| listener | `Listener` | 要传入的Listener对象 |        |

#### frame.setSkin()

> 设置默认皮肤 (不建议使用此功能,可能引起无法对齐等问题)

|   参数   |  类型  |         说明         | 默认值 |
| :------: | :----: | :------------------: | :----: |
| skinList | `List` | 要传入的窗口皮肤List |        |



### Window

Window是一个DUI界面最重要部分，它由开发者自行设计。一个DUI界面可以有多个Window且可以灵活地互相切换，由用户操作按钮来操控。
Window实际上可以单独使用,所有方法都是可以直接调用执行的,即脱离Frame单独显示

#### Window()

> 获取一个窗口对象

|  参数  |  类型  |             说明             |       默认值        |
| :----: | :----: | :--------------------------: | :-----------------: |
| title  | `str`  | 窗口上边框左侧显示的窗口名称 |                     |
| width  | `int`  |           窗口宽度           |         30          |
| height | `int`  |           窗口高度           |         20          |
| system | `int`  |     0为Windows 1为Linux      |          0          |
|  skin  | `List` |          窗口的皮肤          | defaultSkin4Windows |

#### window.addWidget()

> 添加一个控件

|  参数  |   类型   |       说明       | 默认值 |
| :----: | :------: | :--------------: | :----: |
|  line  |  `int`   |   在窗口第几行   |        |
| widget | `Widget` | 要添加的控件对象 |        |

#### window.updateWidget()

> 更新一个控件

|  参数  |   类型   |        说明        | 默认值 |
| :----: | :------: | :----------------: | :----: |
|  line  |  `int`   |    在窗口第几行    |        |
| widget | `Widget` | 要更新的新控件对象 |        |

#### window.showWindow()

> 显示窗口**(可以但不建议直接使用)**



### Listener

Listener是一个DUI界面用户操作部分监听工具，按钮、输入框等控件由Listener控制，最后返回给Frame。

#### Listener()

| 参数 |  类型  |              说明               | 默认值 |
| :--: | :----: | :-----------------------------: | :----: |
| dict | `Dict` |         监听的关键字表          |   {}   |
| mode | `int`  | 监听器的类型:0为python内置input |   0    |

dict例子:

```python
dict = \
	{
		"quit": quit,
		"w": mainWindow.up,
		"s": mainWindow.down,
		"y": listen.confirm
	}
```

在dict中，dict为字典类型，key为`监听的关键字`,value为`运行的函数`

#### listener.setDict()

> 设置Listener的关键字表

| 参数 |  类型  |      说明      | 默认值 |
| :--: | :----: | :------------: | :----: |
| dict | `Dict` | 监听的关键字表 |        |

#### listener.getText()

> 即原生的input，默认以 -> 标记输入

#### listener.run()

> 运行监听器(可以与while True一起使用)

### Alert

​	Alert是一个DUI界面在Window下一行的提示语。(此功能尚未完善)

### Widget

​	Widget为Window服务，可以调用Listener和Alert，最后组成一个开发者需要的组件。Widget为开发者提供基础的对象，开发者可以通过Widget对象扩展新的控件来充实自己的DUI界面。

​	DUI内置一个Text控件，继承自Widget类，开发者可以根据Text控件的写法来自行编写新的插件。

#### Widget

> 基本的控件父类，所有控件继承自Widget，所有属性有get/set方法

|    属性     | 类型  |     说明     | 默认值 |
| :---------: | :---: | :----------: | :----: |
| widget_type | `str` | 标记控件类型 |        |
|     id      | `str` |    控件id    |  None  |

#### Text(Widget)

> 文字控件,继承自Widget

| 参数 | 类型  |              说明               | 默认值 |
| :--: | :---: | :-----------------------------: | :----: |
| text | `str` |          要显示的内容           |   “”   |
| type | `int` | 显示方式: 0左对齐 1居中 2右对齐 |   0    |
|  id  |  str  |               id                |  None  |

##### Text.setText()

| 参数 | 类型  |              说明               | 默认值 |
| :--: | :---: | :-----------------------------: | :----: |
| text | `str` |          要显示的内容           |        |
| type | `int` | 显示方式: 0左对齐 1居中 2右对齐 |   0    |

##### Text.setType()

| 参数 | 类型  |              说明               | 默认值 |
| :--: | :---: | :-----------------------------: | :----: |
| type | `int` | 显示方式: 0左对齐 1居中 2右对齐 |        |

#### Button(Text)

> 按钮控件,继承自Text

|  参数   |    类型    |     说明     | 默认值 |
| :-----: | :--------: | :----------: | :----: |
|  text   |   `str`    | 要显示的内容 |   “”   |
| onClick | `function` | 按钮点击事件 |  None  |
|   id    |    str     |      id      |  None  |

