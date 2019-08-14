## GUI
全程为Graphics User Interface，图形用户界面编程。

### 常见的GUI库

- Tkinter  最基础的GUI库。
- wxPython  比较流行的GUI库，功能强于TKinter。
- PuQT  开源的GUI库，大型的GUI开发。

### TKinter
官方文档地址：https://docs.python.org/3.7/library/tk.html
        		 或者 http://effbot.org/tkinterbook/
         

### GUI编程核心步骤：

- 创建应用程序的主窗口对象
- 在主窗口中，添加可视化组件，比如：按钮(Button)，文本框(Label)等等。
- 通过几何布局管理器，管理组件的大小和位置
- 事件处理

    - 通过绑定事件，响应用户操作所触发的事件，比如：单机双击等等

```python
'''引用于 E:\python_work\python深入与提高\Model\myfirstGUI01.py'''
from tkinter import *
from tkinter import messagebox

# 创建爱你应用程序的主窗口对象
root = Tk()
# 添加可视化组件，这里是Button
btn01 = Button(root)
# 给按钮添加值 
btn01['text'] = '快点我！！'
# 几何布局管理器，管理组件和大小
btn01.pack()

# 绑定事件之编写事件
def dianwo(e):
    # messagebox是一个弹出框。
    messagebox.showinfo('Message','真听话哟~')
    # 控制台打印
    print('让你点你还真点了啊')
# 绑定事件之绑定事件 
btn01.bind('<Button-1>',dianwo)
# 调用组件mainloop方法，进入事件循环 
root.mainloop()
```

### Tkinter 主窗口大小和位置

方法为：geometry('wxh±x±y')
    参数：  w：表示主窗口的宽度。
            h：表示主窗口的高度。
            ±x ：分别表示主窗口距离屏幕左边和右边的距离
            ±y ：分别表示主窗口举例屏幕上边和下边的距离
```python
from tkinter import *
root = Tk()
root.title('确定主窗口的大小和位置')
root.geometry('500x400+100+200')
root.mainloop()
```

### GUI编程整体描述

图形化界面程序的结构是类似于搭积木的情况，一个个组件添加起来组成了整个界面，有的时候还可以在组件里面添加组件等等。
Tkinter 的GUI组成关系是这样的。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190809094703172.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MjAxODY3MQ==,size_16,color_FFFFFF,t_70)

- Misc 和 Wm:是GUI组件的两个父类，直接继承与object
    - Misc ：是所有组件的根父类
    - Wm ：主要提供一些与窗口管理器通信的功能函数。比如Tk()
- Tk() :有Misc和Wm派生出来的子类，代表应用程序的主窗口，一般应用程序都需要直接或者间接使用Tk()
- Pack/Place/Grid ：它们都是布局管理器，是管理组件的大小、位置。
- BaseWidget : 是所有组件的父类
- Widget : 是所有组件类的父类，同时继承与BaseWidget\Pack\Grid\Place，也就是说同时具备这四个父类的全部属性以及方法。

【注】  想观察类的层次结构可以在类定义处的类名上单击右键，选择Diagram-->show
Diagram。

#### 常见组件汇总表

| Tkinter 类  | 名称       | 简介                                                         |
| ----------- | ---------- | ------------------------------------------------------------ |
| Toplevel    | 顶层       | 容器类，可用于为其他组件提供单独的容器；Toplevel 有点类似于窗口 |
| Button      | 按钮       | 代表按钮组件                                                 |
| Canvas      | 画布       | 提供绘图功能，包括直线、矩形、椭圆、多边形、位图等           |
| Checkbutton | 复选框     | 可供用户勾选的复选框                                         |
| Entry       | 单行输入框 | 用户可输入内容                                               |
| Frame       | 容器       | 用于装载其它GUI 组件                                         |
| Label       | 标签       | 用于显示不可编辑的文本或图标                                 |
| LabelFrame  | 容器       | 也是容器组件，类似于Frame，但它支持添加标题                  |
| Listbox     | 列表框     | 列出多个选项，供用户选择                                     |
| Menu        | 菜单       | 菜单组件                                                     |
| Menubutton  | 菜单按钮   | 用来包含菜单的按钮（包括下拉式、层叠式等）                   |
| OptionMenu  | 菜单按钮   | Menubutton 的子类，也代表菜单按钮，可通过按钮打开一个菜单    |
| Message     | 消息框     | 类似于标签，但可以显示多行文本；后来当Label 也能显示多行文本之后，该组件基本处于废弃状态 |
| PanedWindow | 分区窗口   | 该容器会被划分成多个区域，每添加一个组件占一个区域，用户可通过拖动分隔线来改变各区域的大小 |
| Radiobutton | 单选钮     | 可供用户点边的单选钮                                         |
| Scale       | 滑动条     | 拖动滑块可设定起始值和结束值，可显示当前位置的精确值         |
| Spinbox     | 微调选择器 | 用户可通过该组件的向上、向下箭头选择不同的值                 |
| Scrollbar   | 滚动条     | 用于为组件（文本域、画布、列表框、文本框）提供滚动功能       |
| Text        | 多行文本框 | 显示多行文本                                                 |

#### GUI应用程序类经典写法
```python
from tkinter import  * 
from tkinter import messagebox
# 通过Application类组织起整个GUI应用程序。
class Application(Frame):
    def __init__(self,master= None):
        # 继承父类Frame的master.
        super.__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
    def createWidget(self):
        btn01 = Button(self,text= '点我啊？',command = self.dianwo)
        btn02 = Button(self,text = '后悔了吧',command = root.destroy)
        btn01.pack()
        btn02.pack()
    def dianwo(self):
        messagebox.showinfo('hahah','愚蠢的人类')

if __name__ == '__main__':
    root = Tk()
    root.title('第一个GUI程序')
    root.geometry('200x300+200+200')
    # 调用Application函数
    app = Application(master= root)
    root.mainloop()
```
#### 简单组件
##### Label标签
用于显示文本信息，也可以显示图像
常见属性：

- width,height : 指定区域的大小，如果显示的是文本，则以单个字符大小为单位（汉字占两个组字符位置）；如果是图像，则以像素为单位，默认值是根据具体显示的内容动态调整。
- font :指定字体和其大小，font = (font_name,size)
- image :在Label上显示图像，目前tkinter只支持gif格式
- fg 和 bg : fg 为前景色（foreground） bg为背景色（background）
- justify : 针对多行文字的对齐，可以设置为left/right/center
- borderwidth : 文本框框的宽度
- relief : 边框的样式，可以为SUNKEN, RAISED, GROOVE, RIDGE
- compound : 设置成字体和图片混合显示
  
   - center：文字覆盖在图像上
   - left：    图像居左 
   - right:    图像居右 
   - top：     图像居上 
   - bottom：  图像居下

```python
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWedget()

    def createWedget(self):
        '''创建组件'''
        global photo
        photo = PhotoImage(file='images/wallhaven-eye2zo.gif')
        self.label01 = Label(self, text='哈哈哈\n哈哈哈\n哈？', width=20, height=2, font=('黑体', 30), fg='yellow', bg='green',
                             justify=RIGHT, borderwidth=5, relief=GROOVE)
        self.label01.pack()
        # 修改label01信息
        self.label01['text'] = '我改了'
        self.label01.config(fg='red', bg='grey')
        self.label01['font'] = ('楷体', 25)
        self.label02 = Label(self, image=photo)
        self.label02.pack()


if __name__ == '__main__':
    root = Tk()
    root.title('Label的使用')
    root.geometry('400x400+20+20')
    app = Application(master=root)
    root.mainloop()

```

##### Option选项详解
这个option选项可以理解为参数，也就是在创建组件中的width,height,font等等这样的属性。
其实我们可以通过三种方式来设定Option选项
 - 创建对象时的可变参数
 - 创建对象后，使用字典索引方式修改或者添加
 - 创建对象后，config()

查看组件Option选项的方法

- 通过打印config() 方法的返回值，查看  print(fred.config)
- 通过IDE,点击组件对象的构造方法，进入方法中查看

详细的信息如下图

|  选项名（别名） |  含义   |
| ---- | ---- |
|activebackground|   指定组件处于激活状态时的背景色  |
|activeforeground|   指定组件处于激活状态时的前景色   |
|anchor|  指定组件内的信息（比如文本或图片）在组件中如何显示(当所在组件比信息大时，可以看出效果)。必须为下面的值之一：N、NE、E、SE、S、SW、W、NW 或CENTER。比如NW（NorthWest）指定将信息显示在组件的左上角    |
|background(bg)|  指定组件正常显示时的背景色    |
|bitmap|   指定在组件上显示该选项指定的位图，该选项值可以是Tk_GetBitmap接收的任何形式的位图。位图的显示方式受anchor、justify 选项的影响。如果同时指定了bitmap 和text，那么bitmap 覆盖文本；如果同时指定了bitmap 和image，那么image 覆盖bitmap   |
|borderwidth|  指定组件正常显示时的3D 边框的宽度，该值可以是Tk_GetPixels 接收的任何格式    |
|cursor| 指定光标在组件上的样式。该值可以是Tk_GetCursors 接受的任何格式     |
|command|指定按组件关联的命令方法，该方法通常在鼠标离开组件时被触发调用      |
|disabledforeground|指定组件处于禁用状态时的前景色      |
|font | 指定组件上显示的文本字体     |
|foreground(fg)| 指定组件正常显示时的前景色     |
|highlightbackground |指定组件在高亮状态下的背景色      |
|highlightcolor| 指定组件在高亮状态下的前景色     |
|highlightthickness |指定组件在高亮状态下的周围方形区域的宽度，该值可以是Tk_GetPixels 接收的任何格式      |
|height|指定组件的高度，以font 选项指定的字体的字符高度为单位，至少为1      |
|image |指定组件中显示的图像，如果设置了image 选项，它将会覆盖text、bitmap 选项      |
|justify | 指定组件内部内容的对齐方式，该选项支持LEFT（左对齐）、CENTER（居中对齐）或RIGHT（右对齐）这三个值     |
|padx | 指定组件内部在垂直方向上两地的空白，该值可以是Tk_GctPixels 接收的任何格式     |
|pady |指定组件的3D 效果，该选项支持的值包括RAISED、SUNKEN、FLAT、RIDGE、SOLID、GROOVE。该值指出组件内部相对于外部的外观样式，比如RAISED 表示组件内部相对于外部凸起      |
|selectbackground | 指定组件在选中状态下的背景色     |
|selectborderwidth |指定组件在选中状态下的3D 边框的宽度，该值可以是Tk_GetPixels接收的任何格式      |
|selectforeground |指定组在选中状态下的前景色      |
|state |指定组件的当前状态。该选项支持NORMAL（正常）、DISABLE（禁用）这两个值      |
|takefocus |指定组件在键盘遍历（Tab 或Shift+Tab）时是否接收焦点，将该选项设为1 表示接收焦点；设为0 表示不接收焦点      |
|text|指定组件上显示的文本，文本显示格式由组件本身、anchor 及justify 选项决定      |
|textvariable |指定一个变量名，GUI 组件负责显示该变量值转换得到的字符串，文本显示格式由组件本身、anchor 及justify 选项决定      |
|underline|指定为组件文本的第几个字符添加下画线，该选项就相当于为组件绑定了快捷键      |
|width |指定组件的宽度，以font 选项指定的字体的字符高度为单位，至少为1      |
|wraplength |对于能支持字符换行的组件，该选项指定每行显示的最大字符数，超过该数量的字符将会转到下行显示      |
|xscrollcommand | 通常用于将组件的水平滚动改变（包括内容滚动或宽度发生改变）与水平滚动条的set 方法关联，从而让组件的水平滚动改变传递到水平滚动条     |
|yscrollcommand | 通常用于将组件的垂直滚动改变（包括内容滚动或高度发生改变）与垂直滚动条的set 方法关联，从而让组件的垂直滚动改变传递到垂直滚动条     |


##### Button
Button(按钮)用来执行用户的单击操作，Button可以包含文本，也可以包含图像，按钮点击后会自动调用对应事件绑定的方法。
```python
from tkinter import *
from tkinter import messagebox
class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creatWidget()
    def creatWidget(self):
        self.btn01 = Button(self, text='登录', width=6, height=2, justify=CENTER, command=self.login)
        self.btn01.pack()

        global photo
        photo = PhotoImage(file=开始.gif)
        self.btn02 = Button(self, image=photo, command=self.login)
        self.btn02.pack()
        #     设置该按钮为禁用
        self.btn02.config(state='disabled')
        
    def login(self):
        messagebox.showinfo('登录成功')
if __name__ == '__main__':
    root = Tk()
    root.title('Button使用')
    root.geometry('500x500+10+10')
    app = Application(master = root)
    root.mainloop()

```

##### Entry 单行文本框
Entry是用来接受一行字符串的组件，如果用户输入的文字长度长于Entry 控件的宽度
时, 文字会自动向后滚动。如果想输入多行文本, 需要使用Text 控件。
```python
from tkinter import *
from tkinter import  messagebox
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        '''创建登录页面的组件'''
        self.label01 = Label(self, text='用户名')
        self.label01.pack()

        '''StringVar 变量绑定到指定的组件上，当StringVar的值发生变化时，组件的值也发生变化，组件内容变化，StringVar的值也变化'''
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()
        # 默认为admin
        v1.set('admin')

        print(self.entry01.get())

        '''创建密码框'''
        self.label02 = Label(self, text='密码')
        self.label02.pack()

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2)
        self.entry02.pack()
        print(self.entry02.get())

        Button(self, text="登陆", command=self.login).pack()

    def login(self):
        user_name = self.entry01.get()
        pwd = self.entry02.get()
        if user_name == '123' and pwd == '123':
            messagebox.showinfo('提示', '登录成功')
        else:
            messagebox.showinfo('提示', '用户名或密码错误')


if __name__ == '__main__':
    root = Tk()
    root.title('Entry单行文本框的使用')
    root.geometry('400x130+200+200')
    app = Application(master=root)
    root.mainloop()
```
##### Text 多行文本框
是用于显示多行文本的，还可以显示网页链接，HTML页面，添加组件等等，经常被当做简单的文本处理器，文本编辑器或者浏览器来使用，IDLE就是由Text组件构成的。
```python
class Application():
    # 初始化方法和之前一样，不赘述
    def createWidget(self):
        self.text01 = Text(self, width=40, height=12, bg='gray')
        self.text01.pack()
        self.text01.insert(1.0, '从1.1开始')
        self.text01.insert(2.3, '   那我就是2.3')
        Button(self, text='重复插入文本', command=self.insertText).pack(side='left')
        Button(self, text='返回文本', command=self.returnText).pack(side='left')
        Button(self, text='插入图片', command=self.addImage).pack(side='left')
        Button(self, text='添加组件', command=self.addWidget).pack(side='left')

    def insertText(self):
        # INSERT 表示在光标的地方插入
        self.text01.insert(INSERT, '666')
        # END 表示在最后插入
        self.text01.insert(END, '最后了~')
        self.text01.insert(1.8, '在第一行第八个字符处插入')

    def returnText(self):
        # Index(索引)是用来指向Text组件中文本的位置的，Text的组件索引也是对应实际字符之间的位置
        # 核心：行号以1开始，列号从0开始
        print(self.text01.get(2.2, 2.6))
        # 上行代码解释：2.2，2.6-->从第二行的第二个字符开始到第二行的第六个字符
        print('所有文本内容\n' + self.text01.get(1.0, END))

    def addImage(self):
        '''
        增加图片，这里图片不用设置为全局变量，使用Text组件中的image_create函数
        '''
        self.photo = PhotoImage(file='images/start.gif')
        self.text01.image_create(END, image=self.photo)

    def addWidget(self):
        '''
        添加组件,使用Text组件中的window_create函数
        '''
        btn01 = Button(self, text='我是实验')
        self.text01.window_create(INSERT, window=btn01)

```

###### 利用Tags实现更加强大的文本显示和控制
Tags通常是改变Text组件中的内容的样式和功能，可以修改字体的大小，尺寸和颜色等等，另外还允许你将文本、嵌入的组件、图片和鼠标和键盘的事件关联起来。
```python
root = Tk()
root.geometry('300x300+400+400')
text01 = Text(root,width=40,height = 20)
text01.pack()
text01.insert(INSERT,'good good study,day day up!\n百度一下，你就知道')
# tag_add方法，可以这么理解，把位置参数之间的作为一个tags对象，add_config是对tags对象生效的
text01.tag_add('哈哈',1.0,1.6)
text01.tag_config('哈哈',background = 'yellow',foreground='red')
text01.tag_add('百度',2.0,2.2)
text01.tag_config('百度',underline =True)
# 增加点击事件的函数
def webshow(event):
    webbrowser.open('http://www.baidu.com')
# 点击执行webshow方法
text01.tag_bind('百度','<Button-1>',webshow)
root.mainloop()
```

##### Radiobutton 单选按钮
Radiobutton 控件用于选择同一组单选按钮中的一个。Radiobutton 可以显示文本，也可以显示图像。
```python
'''选择性别男女'''
def createWidget(self):
    '''Radiobutton单选按钮,创建组件'''
    self.v = StringVar()
    self.v.set('F')
    # variable 表示可变的意思
    self.r1 = Radiobutton(self,text='男性',value='M',variable=self.v)
    self.r2 = Radiobutton(self,text='女性',value='W',variable=self.v)
    self.r1.pack(side='left')
    self.r2.pack(side='left')
    Button(self,text='确定',command=self.confirm).pack(side='left')
def confirm(self):
    messagebox.showinfo('测试','选择性别为：'+self.v.get())
```

##### Checkbutton 复选按钮
复选按钮和单选按钮的区别就在于指定值上面，复选按钮按钮的指定值类型为IntVar。
```python
def createWidget(self):
    '''Checkbotton复选按钮,创建组件'''
    # 需要先创建两个记录值的IntVar()
    self.radioHobby = IntVar()
    self.codeHobby = IntVar()
    # 先打印下看看其中是否有值
    # print(self.radioHobby.get())  # 默认值为0
    # 在Checkbutton复选按钮中，单选框的value变为，选定(onvalue)和不选定(ofvalue)两个方面
    self.c1 = Checkbutton(self, text='娱乐', variable=self.radioHobby, onvalue=1, offvalue=0)
    self.c2 = Checkbutton(self, text='代码', variable=self.codeHobby, onvalue=1, offvalue=0)
    self.c1.pack(side='left')
    self.c2.pack(side='left')
    Button(self,text='提交',command=self.confirm).pack(side='left')
def confirm(self):
    if self.radioHobby.get() == 1 :
        messagebox.showinfo('提示','选定娱乐ok，开始~')
    elif self.codeHobby.get()== 1 :
        messagebox.showinfo('提示', '选定娱乐ok，开始~')
    else:
        messagebox.showerror('警告','请选择一项')
```

##### canvas 画布
canvas 是一个矩形区域，可以放置图形、图像、组件等。
```python
def createWidget(self):
    '''canvas画布'''
    self.c1 = Canvas(self,width=300,height=300,bg='green')
    self.c1.pack()
    # 一条直线 分为三个点，（10,10）->(30,20)->(40,50)
    line = self.c1.create_line(10,10,30,20,40,50)
    # 画一个矩形 通过两个点来确定，左上角的点（50,50） 和右下角的点（100,100）
    rect = self.c1.create_rectangle(50,50,100,100)
    # 画一个椭圆(圆)  坐标两双。为椭圆的边界矩形左上角和底部右下角
    oval = self.c1.create_oval(50,50,100,100)
    # 添加图片
    global  photo
    photo = PhotoImage(file='images/start.gif')
    # 定义的位置为图片的中心点的坐标
    self.c1.create_image(300,300,image=photo)
    # 画10个矩形
    Button(self,text='10个矩形哦~',command=self.draw).pack(side='left')
def draw(self):
    for i in range(1,10):
        # 分别指定四个坐标的位置
        x1 = random.randrange(int(self.c1['width'])/2)
        y1 = random.randrange(int(self.c1['height'])/2)
        x2 = x1+ random.randrange(int(self.c1['width'])/2)
        y2 = y1+ random.randrange(int(self.c1['height'])/2)
        self.c1.create_rectangle(x1,y1,x2,y2)
```

### 布局管理器
布局管理器是帮助我们组织、管理在父组件中的子组件的布局方式，分别为三种管理器（pack、grid、place）
#### gird
gird布局管理器是采用了表格结构的组织组件，**子组件的位置是由行和列的单元格来确定**，并且也可以跨行或者跨列，从而实现复杂的布局方式
gird()方法提供的选项
|选项|说明|取值范围|
| ---- | ---- | ---- |
|column|单元格的列号|从0 开始的正整数|
|columnspan|跨列，跨越的列数      |正整数      |
|row|单元格的行号      |从0 开始的正整数      |
|rowspan|跨列，跨越的行数      |正整数      |
|ipadx, ipady|设置子组件之间的间隔，x 方向或者y 方向，默认单位为像素      |非负浮点数，默认0.0      |
|padx, pady|与之并列的组件之间的间隔，x 方向或者y 方向，默认单位是像素      |非负浮点数，默认0.0      |
|sticky|组件紧贴所在单元格的某一角，对应于东南西北中以及4 个角      |“n”, “s”, “w”, “e”,“nw”, “sw”, “se”,“ne”, “center”(默认)      |

```python
''''grid 布局用法-登录界面设计'''
class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
    def createWidget(self):
        '''利用gird来布局，分为三行三列，（0，0）（0,1）(0,2)等等'''
        self.label1 = Label(self,text='用户名')
        self.label1.grid(row=0,column=0)
        self.entry1= Entry(self)
        self.entry1.grid(row=0,column =1)
        Label(self,text='用户名为手机号').grid(row=0,column = 2)
        Label(self, text="密码").grid(row=1, column=0)
        Entry(self, show="*").grid(row=1, column=1)
        Button(self, text="登录").grid(row=2, column=1, sticky=EW)
        Button(self, text="取消").grid(row=2, column=2, sticky=E)

'''通过grid 布局-实现计算器软件界面'''
class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()
    def createWidget(self):
        btntext= (("MC","M+","M-","MR"),
                    ("C","±","/","✖ "),
                    (7,8,9,"-"),
                    (4,5,6,"+"),
                    (1,2,3,"="),
                    (0,"."))
        Entry(self).grid(row=0,column = 0,columnspan= 4)
        for rindex,r in enumerate(btntext):
            for cindex,c in enumerate(r):
                if c =='=':
                    Button(self,text=c,width=2).grid(row=rindex+1,column = cindex,rowspan=2,sticky=NSEW)

                elif c == 0 :
                    Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex,columnspan=2,sticky=NSEW)
                elif c =='.':
                    Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex+1,sticky=NSEW)
                else:
                    Button(self,text=c,width=2).grid(row=rindex+1,column=cindex,sticky=NSEW)


```

#### pack 
pack按照组件的创建顺序将子组件添加到父组件里面，按照垂直水平的方向自然排列，如果不指定任何代码，默认是在父组件中自顶而下垂直添加组件，其代码量是最少的。

|选项|说明|取值范围|
| ---- | ---- | ---- |
|expand|当值为yes时，side无效，组件显示在中心位置，若fill选项为'both',填充父组件的剩余空间|'yes',自然数，'no',0(默认为'no'或)|
|fill|填充x(y)方向上的空间，当side='top'或'buttom'填充x 方向;当属性side=”left”或”right”时，填充”y”方向;当expand选项为'yes'时,填充父组件的剩余空间|'x','y','both','none'(默认)|
|ipadx,ipady|设置子组件之间的间隔，x 方向或者y 方向，默认单位为像素|非负浮点数，默认0.0 |
|padx,pady|与之并列的组件之间的间隔，x 方向或者y 方向，默认单位是像素|非负浮点数，默认0.0     |
|side|定义停靠在父组件的哪一边上    |top\bottom\left\right(默认为top)      |
|before|将本组件于所选组建对象之前pack，类似于先创建本组件再创建选定组件      |已经pack 后的组件对象      |
|after|将本组件于所选组建对象之后pack，类似于先创建选定组件再本组件      |已经pack 后的组件对象      |
|in_|将本组件作为所选组建对象的子组件，类似于指定本组件的master 为选定组件      |已经pack 后的组件对象      |
|anchor|对齐方式，左对齐”w”，右对齐”e”，顶对齐”n”底对齐”s”      |w/e/n/s/nw/sw/se/ne/center      |

```python
'''制作钢琴按键布局'''
from tkinter import *
root = Tk()
root.geometry('500x500')
f1 = Frame(root)
f1.pack()
f2 = Frame(root)
f2.pack()
btntext= ("流行风","中国风","日本风","重金属","轻音乐")
for txt in btntext:
    Button(f1,text=txt).pack(side='left',padx= 10)
for i in range(1,20):
    Button(f2,width=3,height=10,bg = 'black' if i%2 == 0 else 'white').pack(side='left')
root.mainloop()

```

#### place 
是通过具体精确的坐标来控制组件的位置的
|选项|说明|取值范围|
| ---- | ---- | ---- |
|x,y|组件左上角的绝对坐标（相对窗口）|非负整数，用于设置偏移，若也设置了relx,那么先计算relx|
|relx,rely|组件左上角的坐标（相对窗口）     |relx相对于父组件的位置，0为最左边，0.5中间，1最右  rely类似      |
|width,height|组件的宽度和高度      |非负整数    |
|relwidth,relheight|组件的宽度和高度（想对于父容器）      |与relx、rely 取值类似，但是相对于父组件的尺寸      |
|anchor|对齐方式，左对齐”w”，右对齐”e”，顶对齐”n”底对齐”s”      |w/e/n/s/nw/sw/se/ne/center（默认）      |

```python
'''扑克游戏demo'''
class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master= master
        self.pack()
        self.createWidget()
    def createWidget(self):
        self.photos = [PhotoImage(file="imgs/puke/puke" + str(i + 1) + ".gif") for i in
                       range(10)]
        self.pukes = [Label(self.master, image=self.photos[i]) for i in range(10)]
        for i in range(10):
            self.pukes[i].place(x=10 + i * 40, y=50)
            # 为所有的Label 增加事件处理
            self.pukes[0].bind_class("Label", "<Button-1>", self.chupai)

    def chupai(self, event):
            print(event.widget.winfo_geometry())

            print(event.widget.winfo_y())
            if event.widget.winfo_y() == 50:
                event.widget.place(y=30)
            else:
                event.widget.place(y=50)
                
```

### 事件处理
一个GUI 应用整个生命周期都处在一个消息循环(event loop) 中。它等待事件的发生，并作出相应的处理。
而Tkinter中提供了用于处理相关事件的机制，处理函数可被绑定给各个控件的各种事件。
----》 widget.bind(event, handler)     如果event发生，handler会被触发，并且事件对象event会传递给handler函数。

#### 鼠标和键盘事件

|代码   | 说明  |
|----|----|----|
| <Button-1>   <ButtonPress-1>   <1>    | 鼠标左键按下   2 表示右键  3 表示中键  |
| <ButtonRelease-1>  | 鼠标左键释放  |
| <B1-Motion>  | 按住鼠标左键移动  |
| <Double-Button-1>  | 双击左键  |
| <Enter>  | 鼠标指针进入某一组件区域  |
| <Leave>  | 鼠标指针离开某一组件区域  |
|<MouseWheel>|滚动滚轮|
|<KeyPress-a>|按下a 键，a 可用其他键替代|
|<KeyRelease-a>|释放a 键。|
|<KeyPress-A>|按下A 键（大写的A）|
|<Alt-KeyPress-a>|同时按下alt 和a；alt 可用ctrl 和shift 替代|
|<Double-KeyPress-a>|快速按两下a|
|<Control-V>|CTRL 和V 键被同时按下，V 可以换成其它键位|

#### event 对象常用属性
|名称|说明|
|----|----|
|char|按键字符，仅对键盘事件有效|
|keycode|按键编码，仅对键盘事件有效|
|keysym|按键名称，仅对键盘事件有效   比如空格键：char ' '  keycode 32 keysym space ；a键 char a  keycode 65 keysym a |
|num|鼠标按键，仅对鼠标事件有效|
|type|所触发的事件类型|
|widget|引起事件的组件|
|width,height|组件改变后的大小，仅Configure 有效|
|x,y|鼠标当前位置，相对于父容器|
|x_root,y_root|鼠标当前位置，相对于整个屏幕|

```python
'''用法测试'''
root = Tk()
root.geometry('530x200')
c1 = Canvas(root,width=200,height=200,bg='green')
c1.pack()

# 鼠标单击测试
def mouseTest(event):
    print('鼠标左键单击位置(相对于父容器)：{0},{1}'.format(event.x,event.y))
    print('鼠标左键单击位置(相对于屏幕)：{0},{1}'.format(event.x_root,event.y_root))
    print('事件绑定的组件：{0}'.format(event.widget))
# 鼠标拖动测试
def testDrag(event):
    '''鼠标拖动产生线'''
    c1.create_oval(event.x,event.y,event.x+1,event.y+1)
# 键盘键入测试
def keyboardTest(event):
    print("键的keycode:{0},键的char:{1},键的keysym:{2}".format(event.keycode,event.char,event.keysym))
#  键入a测试，指定了小写的，那必须是小写的
def press_a_test(event):
    print("press a")
# 释放a键，调用下列函数
def release_a_test(event):
    print("release a")

c1.bind('<Button-1>',mouseTest)
c1.bind('<B1-Motion>',testDrag)
# 键盘事件是针对于root而言的，和画布组件没什么关系
root.bind('<KeyPress>',keyboardTest)
# 当指定了对键入某个值的固定操作后，通用操作就失效了
root.bind('<KeyPress-a>',press_a_test)
#  松开a键测试
root.bind('<KeyRelease-a>',release_a_test)
root.mainloop()

```

#### lambda 表达式详解
lambda定义的是一个匿名函数，适合简单的输入参数，格式为：lambda 参数列表：表达式
比如：
add3args = lambda x,y,z:x+y+z

lambda的参数列表如下
|lambda格式|说明|
|----|----|
|lambda x, y: x*y|函数输入是x 和y，输出是它们的积x*y|
|lambda:None| 函数没有输入参数，输出是None|
|lambda:aaa(3,4)|函数没有输入参数，输出是aaa(3,4)的结果|
|lambda *args: sum(args)|输入是任意个数的参数，输出是它们的和|
|lambda **kwargs: 1|输入是任意键值对参数，输出是1|

##### lambda实现传参

```python
def mouseTest1():
    print("command 方式，简单情况：不涉及获取event 对象，可以使用")
def mouseTest(a,b):
    print("a={0},b={1}".format(a,b))
Button(root, text="测试command1",command=mouseTest1).pack(side="left")
Button(root, text="测试command2",command=lambda: mouseTest2("gaoqi", "xixi")).pack(side="left")
```

### 多种事件绑定方式

- 组件对象的绑定
  
    - 通过command 属性绑定（适合简单不需获取event 对象）：Button(root,text='登录',command=login)
    - 通过bind()方法绑定（适合需要获取event 对象） :c1 = Canvs()   c1.bind('<Button-1>',drawline)

- 组件类的绑定

    - 调用对象的bind_class 函数，将该组件类所有的组件绑定事件  格式： w.bind_class('Widget','event',eventhanler)
    - 比如： btn01.bind_class('Button','<Button-1>',func)
    
```python
def mouseTest1(event):
    print("bind()方式绑定，可以获取event 对象")
    print(event.widget)

def mouseTest2(a, b):
    print("a={0},b={1}".format(a, b))
    print("command 方式绑定，不能直接获取event 对象")

def mouseTest3(event):
    print("右键单击事件，绑定给所有按钮啦！！")
    print(event.widget)
b1 = Button(root, text="测试bind()绑定")
b1.pack(side="left")
# bind 方式绑定事件
b1.bind("<Button-1>", mouseTest1)
# command 属性直接绑定事件
b2 = Button(root, text="测试command2",
command=lambda: mouseTest2("gaoqi", "xixi"))
b2.pack(side="left")
# 给所有Button 按钮都绑定右键单击事件<Button-2>
b1.bind_class("Button", "<Button-2>", mouseTest3)
```

### 其他组件
#### OptionMenu选择项
这个选择项是用来多选一的，选中项会在最上边顶部显示。类似于网页中的下拉框的感觉。
```python
'''optionmenu 的使用测试'''
root = Tk()
root.geometry('500x500')
# 必须要给其指定一个默认值，并且这个默认值不能通过组件参数形式指定
v = StringVar(root)
v.set('我是小天才')
om = OptionMenu(root,v,'太菜','天才个鬼啊')
# OptionMenu中的宽度等等的属性不能再参数中直接指定，得额外指定，包括其布局方式
om['width']= 10
om.pack()
def test():
    print('我成功了',v.get())

Button(root,text='确定',command = test).pack()
root,mainloop()
```
#### Scale 移动滑块
Scale(移动滑块)用于在指定的数值区间，通过滑块的移动来选择值.
```python
root = Tk()
root.geometry('500x500')
def test1(value):
    print('滑块的值：',value)
    newFont = ('楷体',value)
    a.config(font=newFont)
# orient（方向）= HORIZONTAL(水平)  tickinterval(刻度间隔)
s1= Scale(root,from_= 10,to=50,length=200,tickinterval=5,orient= HORIZONTAL,command=test1)
s1.pack()
a = Label(root,text= '哈哈哈',width=10,height=1,bg='black',fg='white')
a.pack()
root,mainloop()
```

#### 颜色选择框(colorchooser+askcolor)
颜色选择框可以帮助我们设置背景色、前景色、画笔颜色、字体颜色等等。
```python
from tkinter.colorchooser import *
root = Tk()
root.geometry('500x500')
def test():
    # 封装好的点击出现颜色选择框
    s1= askcolor(color='red',title='选择背景色')
    print(s1)
    # s1是一个元组，里面第二个才是颜色的代码
    root.config(bg=s1[1])

Button(root,text='选择背景色',command=test).pack()
root.mainloop()
```

#### 文件对话框
实现可视化的操作目录、操作文件，最后，将文件、目录的信息传入到程序中。
|函数名|对话框|说明|
|----|----|----|
|askopenfilename(**options)|文件对话框|返回打开的文件名|
|askopenfilenames(**options)||返回打开的多个文件名列表|
|askopenfile(**options)||返回打开文件对象|
|askopenfiles(**options)||返回打开的文件对象的列表|
|askdirectory(**options)|目录对话框|返回目录名|
|asksaveasfile(**options)|保存对话框|返回保存的文件对象|
|asksaveasfilename(**options)||返回保存的文件名|

命名参数options的常见值
|参数名|说明|
|----|----|
|defaultextension|默认后缀：.XXX    用户没有输入则自动添加|
|filetypes=[(label1,pattern1),(labe2,pattern2)]|文件显示过滤器|
|initialdir|初始目录|
|initialfile|初始文件|
|parent|父窗口，默认根窗口|
|title|标题|
```python
'''基本用法'''
from tkinter.filedialog import *
root = Tk()
root.geometry('500x500')
def test():
    f = askopenfilename(title= '上传文件',initialdir='f:/file',filetypes=[('图片文件','.png')])
    show['text'] = f
Button(root,text="选择编辑的视频文件",command=test).pack()
show = Label(root,width=40,height=3,bg="green")
show.pack()
'''打开指定txt 文件，并读出文件内容到窗口'''
def test1():
    with askopenfile(title="上传文件",initialdir="d:",filetypes=[("文本文件",".txt")]) as f:
    show["text"]=f.read()
Button(root,text="选择读取的文本文件",command=test1).pack()
show = Label(root,width=40,height=3,bg="green")
show.pack()

```

#### 简单输入对话框
simpledialog(简单对话框)包含如下常用函数：
|函数名|说明|
|----|----|
|askfloat(title,prompt,**kw)|输入并返回浮点数|
|askinteger(title,prompt,**kw)|输入并返回整数|
|askstring(title,prompt,**kw)|输入并返回字符串|

参数中，title 表示窗口标题；prompt 是提示信息；命名参数kw 为各种选项：initialvalue（初始值）、minvalue（最小值）、maxvalue（最大值）。
```python
'''简单的对话框'''
from tkinter.simpledialog import *
root = Tk();root.geometry("400x100")
def test1():
    a = askinteger(title="输入年龄",prompt="请输入年龄",initialvalue=18,minvalue=1,maxvalue=150)
    # askstring、askfloat 框使用方式一样
    show["text"]=a
Button(root,text="老高你多大了? 请输入",command=test1).pack()
show = Label(root,width=40,height=3,bg="green")
show.pack()
root.mainloop()
```

#### 通用信息框
messagebox（通用消息框）用于和用户简单的交互，用户点击确定、取消。
|函数名|说明|
|----|----|
|askokcancel(title,message,**options)|OK/Cancel 对话框|
|askquestion(title,message,**options)|Yes/No 问题对话框|
|askretrycancel(title,message,**options)|Retry/Cancel 问题对话框|
|showerror(title,message,**options)|错误消息对话框|
|showinfo(title,message,**options)|消息框|
|showwarning(title,message,**options)|警告消息框|



### ttk 子模块控件
前面学的组件是tkinter 模块下的组件,，整体风格较老较丑,。为了弥补这点不足,推出了ttk 组件。ttk 组件更加美观、功能更加强大,新增了LabeledScale(带标签的
Scale)、Notebook(多文档窗口)、Progressbar(进度条)、Treeview(树)等组件。
#### 菜单
GUI 程序通常都有菜单，方便用户的交互。我们一般将菜单分为两种：

- 主菜单 通常位于GUI 程序上方
- 快捷菜单（上下文菜单）  通过鼠标右键单击某个组件对象而弹出的菜单，一般是与该组件相关的操作。

##### 主菜单
主菜单一般包含：文件、编辑、帮助等，位于GUI 窗口的上面。创建主菜单一般有如下4步：

- 创建主菜单栏对象   
	- menubar = tk.Menu(root)
- 创建菜单，并添加到主菜单栏对象  
	- file_menu = tk.Menu(menubar)  
	- menubar.add_cascade(label=”文件”,menu=file_menu)
- 添加菜单项到2 步中的菜单   
	- file_menu.add_command(label=”打开”)  
	- file_menu.add_command(label=”保存”,accelerator=”^p” command=mySaveFile)   
	- file_menu.add_separator()   
	- file_menu.add_command(label=”退出”)
- 将主菜单栏添加到根窗口  
	- root[“menu”]=menubar

```python
"""开发记事本软件的菜单"""
from tkinter.filedialog import *
from tkinter.colorchooser import *
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.textpad = None    # textpad 表示Text 文本框对象
        self.pack()
        self.createWidget()
    def createWidget(self):
        # 创建主菜单栏
        menubar = Menu(root)
        # 创建子菜单
        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)
        # 将子菜单加入到主菜单栏
        menubar.add_cascade(label="文件(F)", menu=menuFile)
        menubar.add_cascade(label="编辑(E)", menu=menuEdit)
        menubar.add_cascade(label="帮助(H)", menu=menuHelp)
        # 添加菜单项
        menuFile.add_command(label="新建", accelerator="ctrl+n",
                             command=self.test)
        menuFile.add_command(label="打开", accelerator="ctrl+o",
                             command=self.test)
        menuFile.add_command(label="保存",
                             accelerator="ctrl+s",command=self.test)
        menuFile.add_separator() # 添加分割线
        menuFile.add_command(label="退出",
                             accelerator="ctrl+q",command=self.test)
        # 将主菜单栏加到根窗口
        root["menu"] = menubar
        #文本编辑区
        self.textpad = Text(root, width=50, height=30)
        self.textpad.pack()
    def test(self):
        pass
if __name__ == '__main__':
	root = Tk()
	root.geometry("450x300+200+300")
	root.title("简易记事本")
	app = Application(master=root)
	root.mainloop()
```

##### 上下文菜单
快捷菜单（上下文菜单）是通过鼠标右键单击组件而弹出的菜单，一般是和这个组件相关的操作，比如：剪切、复制、粘贴、属性等。创建快捷菜单步骤如下：

- 创建菜单

	- menubar = tk.Menu(root)
	- menubar.add_command(label=”字体”)

- 绑定鼠标右键单击事件

	- ```python
		def test(event):
			menubar.post(event.x_root,event.y_root) #在鼠标右键单击坐标处显示菜单
		root.bind(“<Button-3>”,test)
		```
```python
'''为记事本程序增加上下文菜单'''
from tkinter import *
from tkinter.colorchooser import *
from tkinter.filedialog import *
root = Tk();root.geometry("400x400")
def openAskColor():
    s1 = askcolor(color="red", title="选择背景色")
    root.config(bg=s1[1])
#创建快捷菜单
menubar2 = Menu(root)
menubar2.add_command(label="颜色",command=openAskColor)
menuedit = Menu(menubar2,tearoff=0)
menuedit.add_command(label="剪切")
menuedit.add_command(label="复制")
menuedit.add_command(label="粘贴")
menubar2.add_cascade(label="编辑",menu=menuedit)
def test(event):
    #菜单在鼠标右键单击的坐标处显示
    menubar2.post(event.x_root,event.y_root)
#编辑区
w1 = Text(root,width=50,height=30)
w1.pack()
w1.bind("<Button-3>",test)
root.mainloop()
```

### 项目开发

结合所学GUI 知识，开发一款模仿windows 记事本的软件。包含了基本的功能：

1. 新建文本文件
2. 保存文件
3. 修改文件内容
4. 退出
5. 各种快捷键处理
6. 修改文本区域背景
见test.py文件

#### 将python 程序打包成exe 文件
使用pyinstaller 包导出，在Terminal控制台输入pyinstaller -F XXX.py
相关参数为：
1、 --icon = 图表路径（pyinstaller -F --icon=my.ico XXX.py）
2、-F  打包成一个exe文件
3、-w  使用窗口，无控制台
4、-c  使用控制台，无窗口
5、-D  创建一个目录，里面包含exe 以及其他一些依赖性文件

【注意】  现在pyinstaller只支持python3.6，不支持py3.7

#### 画图软件开发
开发一款简单的画图软件, 包含如下功能：
1. 画笔
2. 矩形/椭圆绘制
3. 清屏
4. 橡皮擦
5. 直线/带箭头的直线
6. 修改画笔颜色、背景颜色

见draw.py
 

