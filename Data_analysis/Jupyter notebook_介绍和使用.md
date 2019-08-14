### Jupyter notebook

jupyter notebook是一款开源web应用程序，该应用程序看创建并实施代码，可视化以及文本说明。jupyter notebook基于IPython解释器，是一个基于we的交互式计算环境。之前名称叫做IPython notebook。

#### 启动jupyter

控制台输入命令：jupyter notebook(jupyter-notebook)

Anaconda程序菜单启动

启动后，启动jupyter服务，同时打开浏览器页面，显示jupyter的home页面。默认情况下，使用当前用户目录为根目录

#### 停止jupyter

控制台输入命令：ctrl+c

#### 修改默认主目录

类似于pycharm集成开发工具中工作空间，默认是当前用户目录。我们可通过命令行和配置文件2种方式修改

* 命令行

  方法1：切换到文件目录，启动jupyter，文件目录为主目录

  方法2：启动时候设置参数 notebook-dir=c:

* 配置文件

  步骤 1：设置配置文件中c.NotebookApp.notebook_dir参数值主目录信息

  步骤2：快捷方式中设置主目录信息

#### 文件操作

在主目录下，可以jupyter notebook文档(*.ipynb)进行文件操作

* 上传文件
* 新建文件 
* 修改文件名
* 删除文件

#### 单元格

jupyter notebook文档由一些单元格组成，我们可以在单元格中输入相关代码或者说明文字。

##### 类型：

​	code：python代码单元格，用来编写程序

​	Markdown：支持Markdown语法单元格，用来编写描述程序的文字

​	Raw NBConvert：原生类型单元格，内容原样显示。使用NBConvert转换后才会显示特殊格式，基本不用。

​	Heading：标题单元格，已经不再支持。

##### 模式

模式不同，对快捷键支持不同

* 命令模式

* 编辑模式

##### 常用快捷键

命令模式

* Y:单元格转为code类型
* M:单元格转为Markdown类型
* Enter：进入编辑模式

编辑模式：

* tab：代码补全
* esc:进入命令模式

通用模式：

* ctrl+enter:运行单元格，单元格处于命令模式
* shift+enter:运行单元格，并切换到下一个单元格，如下方没有，则新建一个单元格
* alter+enter:运行单元格，并在下方新增一个单元格












