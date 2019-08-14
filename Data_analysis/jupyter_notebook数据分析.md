# Jupyter_notebook

#### 介绍

​		Jupyter_notebook是一款开源的web应用程序，它可以创建、实施代码、以及可视化和文本说明，基于IPython解释器。

##### 启动和关闭

- ###### 启动

  - dos窗口输入`jupyter notebook(或者jupyter-notebook)`。
  - 在Anaconda菜单启动 jupyter notebook。

- ###### 关闭

  - 在弹出的控制台窗口键入`ctrl+c`。

##### 修改默认的主目录文件

​	默认的主目录文件是在打开jupyter notebook后显示的目录，类似于pycharm的开发空间，修改主目录文件方法。

1. 命令行
   1. 切换到文件目录，启动jupyter，那么该目录就为主目录。
   2. 启动的时候设置参数 `notebook-dir = c`。
2. 配置文件（步骤）
   1. 设置配置文件中的`c.NotebookApp.notebook_dir`参数值主目录信息。
   2. 快捷方式中设置主目录信息，把起始位置填入更改的目录

##### 文件操作

- 上传文件   upload
- 新建文件   new
- 修改文件名    关闭之后，rename
- 删除文件     关闭之后，delete

##### 单元格

​	jupyter notebook 文档是有一个个单元格组成的，在单元格中可以输入相应的代码或者说明文字等等。。

###### 类型支持

- Code：也就是python代码
- Markdown：支持Markdown语法单元格，用来编写描述程序的文字
- Raw NBConvert：原生类型单元格，内容原样显示。使用NBConvert转换后才会显示特殊格式，基本不用。
- Heading：标题单元格，已经不再支持。

##### 模式

- 命令模式
- 编辑模式

##### 常用的快捷键(下列的所有的大写字母都是把大写锁打开的`CapsLock`)

###### 命令模式

- Y：单元格转为code类型
- M：单元格转为Markdown类型
- R：转化为Raw NBConvert类型
- Enter：进入编辑模式
- A：上方插入新单元格
- B：下方插入新单元格
- C：复制
- D（两次）：删除单元格
- V：粘贴到当前单元格下方
- Shift+v：粘贴到当前单元格上方
- Z：撤销删除

###### 编辑模式：

- tab：代码补全
- Shift + Tab：显示doc文档信息
- esc：进入命令模式

###### 通用模式：

- ctrl+enter：运行单元格，单元格处于命令模式
- shift+enter：运行单元格，并切换到下一个单元格，如下方没有，则新建一个单元格
- alter+enter：运行单元格，并在下方新增一个单元格







  