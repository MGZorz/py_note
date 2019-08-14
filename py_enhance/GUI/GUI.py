from tkinter import *
from tkinter import messagebox
import webbrowser
import random

'''第一个简单的GUI程序'''
# # 创建窗口化对象
# root = Tk()
# # 添加可视化组件，可以互动的那种
# btn01 = Button(root)
# btn01['text'] = '点我啊~'
# # 调整可视化组件位置
# btn01.pack()
# # 绑定事件之编写事件
# def dianwo(e):
#     # messagebox ：点击弹出框
#     messagebox.showinfo('Message','真听话~')
#     # 控制台打印
#     print('让你点就点啊')
#
# # 绑定事件，由Button绑定
# btn01.bind('<Button-1>',dianwo)
#
# # 进入事件循环，没有这个就显示不出来
# root.mainloop()
'''Tkinter 主窗口位置和大小'''
# root = Tk()
#
# root.title('测试大小')
# # 规定主窗口大小以及位置
# root.geometry('500x400+100+200')
# root.mainloop()
'''简单的经典的GUI应用程序'''
# class Application(Frame):
#     '''一个经典的GUI程序的类的写法'''
#
#     def __init__(self, master=None):
#         super().__init__(master)  # super()代表的是父类的属性，而不是方法
#         self.master = master
#         self.pack()
#         self.createWidget()
#
#     def createWidget(self):
#         '''创建组件'''
#         btn01 = Button(self, text='点我哦！', command=self.dianwo)
#         btn01.pack()
#         # 创建一个退出按钮   root.destroy 表示退出
#         btn02 = Button(self, text='退出', command=root.destroy)
#         btn02.pack()
#
#     def dianwo(self):
#         messagebox.showinfo('真傻呀?', 'hahahah')
#
#
# if __name__ == '__main__':
#     root = Tk()
#     # 位置
#     root.geometry('200x400+200+500')
#     # 标题
#     root.title('经典简单的GUI程序')
#     # 创建一个对象，application传入master
#     app = Application(master=root)
#     root.mainloop()
'''测试Label组件的基本用法，使用面向对象的方法'''
# class Application(Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.createWedget()
#
#     def createWedget(self):
#         '''创建组件'''
#         '''label的属性都有：text 文本信息    width 文本宽度    height 文本的高度      bg  背景颜色    fg 前景颜色(文字颜色)
#                     font 字体属性(字体，字号)'''
#         self.label01 = Label(self, text='我是Label', width=10, height=2, bg='black', fg='yellow', font=('黑体', 30))
#         # 修改text内容，fg/bg属性，font属性
#         self.label01['text'] = '哈哈哈'
#         self.label01.config(fg='red', bg='green')
#         self.label01.pack()
#         self.label01['font'] = ('黑体', 30)
#
#         # 显示图像+ 显示多行文本
#         global photo  # 把photo 声明成全局变量。如果是局部变量，本方法执行完毕后，图像对象销毁，窗口显示不出图像。
#         photo = PhotoImage(file='images/wallhaven-eye2zo.gif')  # 注意只能是gif图像哦
#         # borderwidth 文本框宽度    relief 边框的样式（SUNKEN, RAISED, GROOVE, RIDGE）      justify 文本对齐方式      compound = CENTER 设置文本和图像的混合模式
#         self.label03 = Label(self, image=photo, text='哈哈哈\n额\n哈哈哈哈', borderwidth=5, relief=GROOVE, justify=RIGHT,
#                              compound=CENTER)
#         self.label03.pack()
#
#
# if __name__ == '__main__':
#     root = Tk()
#     root.title('测试Label组件的使用')
#     root.geometry('500x500+300+300')
#     app = Application(master=root)
#     root.mainloop()
'''Button组件的相关使用'''
# class Application(Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.createWidget()
#
#     def createWidget(self):
#         '''创建组件'''
#         self.btn01 = Button(self, text='登录', width=6, height=2, justify=CENTER, command=self.login)
#         self.btn01.pack()
#
#         global photo
#         photo = PhotoImage(file='images/start.gif')
#         self.btn02 = Button(self, image=photo, command=self.login)
#         self.btn02.pack()
#         #     设置该按钮为禁用
#         self.btn02.config(state='disabled')
#
#     def login(self):
#         messagebox.showinfo('登录成功', '欢迎来到同性交友网站')
#         print('登陆成功')
#
# if __name__ == '__main__':
#     root = Tk()
#     root.title('Button的相关使用')
#     root.geometry('500x500+200+200')
#     app = Application(master=root)
#     root.mainloop()
'''Entry单行文本框的使用'''
# class Application(Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.createWidget()
#
#     def createWidget(self):
#         '''创建登录页面的组件'''
#         self.label01 = Label(self, text='用户名')
#         self.label01.pack()
#
#         '''StringVar 变量绑定到指定的组件上，当StringVar的值发生变化时，组件的值也发生变化，组件内容变化，StringVar的值也变化'''
#         v1 = StringVar()
#         self.entry01 = Entry(self, textvariable=v1)
#         self.entry01.pack()
#         # 默认为admin
#         v1.set('admin')
#
#         print(self.entry01.get())
#
#         '''创建密码框'''
#         self.label02 = Label(self, text='密码')
#         self.label02.pack()
#
#         v2 = StringVar()
#         self.entry02 = Entry(self, textvariable=v2)
#         self.entry02.pack()
#         print(self.entry02.get())
#
#         Button(self, text="登陆", command=self.login).pack()
#
#     def login(self):
#         user_name = self.entry01.get()
#         pwd = self.entry02.get()
#         if user_name == '123' and pwd == '123':
#             messagebox.showinfo('提示', '登录成功')
#         else:
#             messagebox.showinfo('提示', '用户名或密码错误')
#
#
# if __name__ == '__main__':
#     root = Tk()
#     root.title('Entry单行文本框的使用')
#     root.geometry('400x130+200+200')
#     app = Application(master=root)
#     root.mainloop()
'''Text多行文本框的的使用'''
# class Application(Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.createWidget()
#
#     def createWidget(self):
#         self.text01 = Text(self, width=40, height=12, bg='gray')
#         self.text01.pack()
#         self.text01.insert(1.0, '从1.1开始')
#         self.text01.insert(2.3, '   那我就是2.3')
#         Button(self, text='重复插入文本', command=self.insertText).pack(side='left')
#         Button(self, text='返回文本', command=self.returnText).pack(side='left')
#         Button(self, text='插入图片', command=self.addImage).pack(side='left')
#         Button(self, text='添加组件', command=self.addWidget).pack(side='left')
#
#     def insertText(self):
#         # INSERT 表示在光标的地方插入
#         self.text01.insert(INSERT, '666')
#         # END 表示在最后插入
#         self.text01.insert(END, '最后了~')
#         self.text01.insert(1.8, '在第一行第八个字符处插入')
#
#     def returnText(self):
#         # Index(索引)是用来指向Text组件中文本的位置的，Text的组件索引也是对应实际字符之间的位置
#         # 核心：行号以1开始，列号从0开始
#         print(self.text01.get(2.2, 2.6))
#         # 上行代码解释：2.2，2.6-->从第二行的第二个字符开始到第二行的第六个字符
#         print('所有文本内容\n' + self.text01.get(1.0, END))
#
#     def addImage(self):
#         '''
#         增加图片，这里图片不用设置为全局变量，使用Text组件中的image_create函数
#         '''
#         self.photo = PhotoImage(file='images/start.gif')
#         self.text01.image_create(END, image=self.photo)
#
#     def addWidget(self):
#         '''
#         添加组件,使用Text组件中的window_create函数
#         '''
#         btn01 = Button(self, text='我是实验')
#         self.text01.window_create(INSERT, window=btn01)
#
#
# if __name__ == '__main__':
#     root = Tk()
#     root.title('Text多行文本框的选择')
#     root.geometry('300x300+200+200')
#     app = Application(master=root)
#     root.mainloop()
'''Tags实现强大的文本显示和控制'''
# root = Tk()
# root.geometry('300x300+400+400')
# text01 = Text(root,width=40,height = 20)
# text01.pack()
# text01.insert(INSERT,'good good study,day day up!\n百度一下，你就知道')
# # tag_add方法，可以这么理解，把位置参数之间的作为一个tags对象，add_config是对tags对象生效的
# text01.tag_add('哈哈',1.0,1.6)
# text01.tag_config('哈哈',background = 'yellow',foreground='red')
# text01.tag_add('百度',2.0,2.2)
# text01.tag_config('百度',underline =True)
# # 增加点击事件的函数
# def webshow(event):
#     webbrowser.open('http://www.baidu.com')
# # 点击执行webshow方法
# text01.tag_bind('百度','<Button-1>',webshow)
# root.mainloop()
'''Radiobutton单选按钮'''
# class Application(Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.createWidget()
#     def createWidget(self):
#         '''Radiobutton单选按钮,创建组件'''
#         self.v = StringVar()
#         self.v.set('F')
#         self.r1 = Radiobutton(self,text='男性',value='M',variable=self.v)
#         self.r2 = Radiobutton(self,text='女性',value='W',variable=self.v)
#         self.r1.pack(side='left')
#         self.r2.pack(side='left')
#         Button(self,text='确定',command=self.confirm).pack(side='left')
#     def confirm(self):
#         messagebox.showinfo('测试','选择性别为：'+self.v.get())
#
# if __name__ == '__main__':
#     root = Tk()
#     root.title('Radiobutton单选按钮')
#     root.geometry('300x300+200+200')
#     app = Application(master=root)
#     root.mainloop()
'''Checkbotton复选按钮'''
# class Application(Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.createWidget()
#
#     def createWidget(self):
#         '''Checkbotton复选按钮,创建组件'''
#         # 需要先创建两个记录值的IntVar()
#         self.radioHobby = IntVar()
#         self.codeHobby = IntVar()
#         # 先打印下看看其中是否有值
#         # print(self.radioHobby.get())  # 默认值为0
#         # 在Checkbutton复选按钮中，单选框的value变为，选定(onvalue)和不选定(ofvalue)两个方面
#         self.c1 = Checkbutton(self, text='娱乐', variable=self.radioHobby, onvalue=1, offvalue=0)
#         self.c2 = Checkbutton(self, text='代码', variable=self.codeHobby, onvalue=1, offvalue=0)
#         self.c1.pack(side='left')
#         self.c2.pack(side='left')
#         Button(self,text='提交',command=self.confirm).pack(side='left')
#     def confirm(self):
#         if self.radioHobby.get() == 1 :
#             messagebox.showinfo('提示','选定娱乐ok，开始~')
#         elif self.codeHobby.get()== 1 :
#             messagebox.showinfo('提示', '选定娱乐ok，开始~')
#         else:
#             messagebox.showerror('警告','请选择一项')
#
#
# if __name__ == '__main__':
#     root = Tk()
#     root.title('Radiobutton单选按钮')
#     root.geometry('300x300+200+200')
#     app = Application(master=root)
#     root.mainloop()
'''canvas 画布'''
# class Application(Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.createWidget()
#
#     def createWidget(self):
#         '''canvas画布'''
#         self.c1 = Canvas(self,width=300,height=300,bg='green')
#         self.c1.pack()
#         # 一条直线 分为三个点，（10,10）->(30,20)->(40,50)
#         line = self.c1.create_line(10,10,30,20,40,50)
#         # 画一个矩形 通过两个点来确定，左上角的点（50,50） 和右下角的点（100,100）
#         rect = self.c1.create_rectangle(50,50,100,100)
#         # 画一个椭圆(圆)  坐标两双。为椭圆的边界矩形左上角和底部右下角
#         oval = self.c1.create_oval(50,50,100,100)
#         # 添加图片
#         global  photo
#         photo = PhotoImage(file='images/start.gif')
#         # 定义的位置为图片的中心点的坐标
#         self.c1.create_image(300,300,image=photo)
#         # 画10个矩形
#         Button(self,text='10个矩形哦~',command=self.draw).pack(side='left')
#     def draw(self):
#         for i in range(1,10):
#             # 分别指定四个坐标的位置
#             x1 = random.randrange(int(self.c1['width'])/2)
#             y1 = random.randrange(int(self.c1['height'])/2)
#             x2 = x1+ random.randrange(int(self.c1['width'])/2)
#             y2 = y1+ random.randrange(int(self.c1['height'])/2)
#             self.c1.create_rectangle(x1,y1,x2,y2)
#
#
# if __name__ == '__main__':
#     root = Tk()
#     root.title('Radiobutton单选按钮')
#     root.geometry('400x400+200+200')
#     app = Application(master=root)
#     root.mainloop()
'''gird布局管理器'''
# 登录界面设置
# class Application(Frame):
#     def __init__(self,master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.createWidget()
#     def createWidget(self):
#         '''利用gird来布局，分为三行三列，（0，0）（0,1）(0,2)等等'''
#         self.label1 = Label(self,text='用户名')
#         self.label1.grid(row=0,column=0)
#         self.entry1= Entry(self)
#         self.entry1.grid(row=0,column =1)
#         Label(self,text='用户名为手机号').grid(row=0,column = 2)
#         Label(self, text="密码").grid(row=1, column=0)
#         Entry(self, show="*").grid(row=1, column=1)
#         Button(self, text="登录").grid(row=2, column=1, sticky=EW)
#         Button(self, text="取消").grid(row=2, column=2, sticky=E)

# 通过grid 布局-实现计算器软件界面。
# 设计一个7行4列的表格布局结构。
# class Application(Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.pack()
#         self.createWidget()
#
#     def createWidget(self):
#         btntext = (("MC", "M+", "M-", "MR"),
#                    ("C", "±", "/", "✖ "),
#                    (7, 8, 9, "-"),
#                    (4, 5, 6, "+"),
#                    (1, 2, 3, "="),
#                    (0, "."))
#         Entry(self).grid(row=0, column=0, columnspan=4)
#         for rindex, r in enumerate(btntext):
#             for cindex, c in enumerate(r):
#                 if c == '=':
#                     Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex, rowspan=2, sticky=NSEW)
#
#                 elif c == 0:
#                     Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex, columnspan=2, sticky=NSEW)
#                 elif c == '.':
#                     Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex + 1, sticky=NSEW)
#                 else:
#                     Button(self, text=c, width=2).grid(row=rindex + 1, column=cindex, sticky=NSEW)
#
#
# if __name__ == '__main__':
#     root = Tk()
#     root.geometry('150x200+200+300')
#     root.title('gird的布局管理')
#     app = Application(master=root)
#     root.mainloop()

'''pack布局管理器'''
# 制作钢琴按键布局
# root = Tk()
# root.geometry('700x220')
# f1 = Frame(root)
# f1.pack()
# f2 = Frame(root)
# f2.pack()
# btnText= ("流行风","中国风","日本风","重金属","轻音乐")
# for txt  in btnText:
#     Button(f1,text=txt).pack(side='left',padx=10)
# for i in range(1,20):
#     # 添加了一个简单的if条件在参数中。
#     Button(f2,width=5,height = 10,bg='black' if i%2==0 else 'white').pack(side='left')
# root.mainloop()
'''place布局管理器'''
# class Application(Frame):
#     def __init__(self,master=None):
#         super().__init__(master)
#         self.master= master
#         self.pack()
#         self.createWidget()
#     def createWidget(self):
#         self.photos = [PhotoImage(file="imgs/puke/puke" + str(i + 1) + ".gif") for i in
#                        range(10)]
#         self.pukes = [Label(self.master, image=self.photos[i]) for i in range(10)]
#         for i in range(10):
#             self.pukes[i].place(x=10 + i * 40, y=50)
#             # 为所有的Label 增加事件处理
#             self.pukes[0].bind_class("Label", "<Button-1>", self.chupai)
#
#     def chupai(self, event):
#             print(event.widget.winfo_geometry())
#
#             print(event.widget.winfo_y())
#             if event.widget.winfo_y() == 50:
#                 event.widget.place(y=30)
#             else:
#                 event.widget.place(y=50)
# if __name__ == '__main__':
#     root = Tk()
#     root.geometry('500x500')
#     app = Application(master=root)
#     root.mainloop()

'''事件处理——鼠标和键盘事件处理'''
# root = Tk()
# root.geometry('530x200')
# c1 = Canvas(root,width=200,height=200,bg='green')
# c1.pack()
#
# # 鼠标单击测试
# def mouseTest(event):
#     print('鼠标左键单击位置(相对于父容器)：{0},{1}'.format(event.x,event.y))
#     print('鼠标左键单击位置(相对于屏幕)：{0},{1}'.format(event.x_root,event.y_root))
#     print('事件绑定的组件：{0}'.format(event.widget))
# # 鼠标拖动测试
# def testDrag(event):
#     '''鼠标拖动产生线'''
#     c1.create_oval(event.x,event.y,event.x+1,event.y+1)
# # 键盘键入测试
# def keyboardTest(event):
#     print("键的keycode:{0},键的char:{1},键的keysym:{2}".format(event.keycode,event.char,event.keysym))
# #  键入a测试，指定了小写的，那必须是小写的
# def press_a_test(event):
#     print("press a")
# # 释放a键，调用下列函数
# def release_a_test(event):
#     print("release a")
#
# c1.bind('<Button-1>',mouseTest)
# c1.bind('<B1-Motion>',testDrag)
# # 键盘事件是针对于root而言的，和画布组件没什么关系
# root.bind('<KeyPress>',keyboardTest)
# # 当指定了对键入某个值的固定操作后，通用操作就失效了
# root.bind('<KeyPress-a>',press_a_test)
# #  松开a键测试
# root.bind('<KeyRelease-a>',release_a_test)
# root.mainloop()

'''Optionmenu 的使用测试'''
# root = Tk()
# root.geometry('500x500')
# # 必须要给其指定一个默认值，并且这个默认值不能通过组件参数形式指定
# v = StringVar(root)
# v.set('我是小天才')
# om = OptionMenu(root,v,'太菜','天才个鬼啊')
# # OptionMenu中的宽度等等的属性不能再参数中直接指定，得额外指定，包括其布局方式
# om['width']= 10
# om.pack()
# def test():
#     print('我成功了',v.get())
#
# Button(root,text='确定',command = test).pack()
# root,mainloop()

'''Scale 移动滑块---根据滑块的调节，其Label的大小'''
# root = Tk()
# root.geometry('500x500')
# def test1(value):
#     print('滑块的值：',value)
#     newFont = ('楷体',value)
#     a.config(font=newFont)
# # orient（方向）= HORIZONTAL(水平)  tickinterval(刻度间隔)
# s1= Scale(root,from_= 10,to=50,length=200,tickinterval=5,orient= HORIZONTAL,command=test1)
# s1.pack()
# a = Label(root,text= '哈哈哈',width=10,height=1,bg='black',fg='white')
# a.pack()
# root,mainloop()

'''颜色选择框'''
# from tkinter.colorchooser import *
# root = Tk()
# root.geometry('500x500')
# def test():
#     # 封装好的点击出现颜色选择框
#     s1= askcolor(color='red',title='选择背景色')
#     print(s1)
#     # s1是一个元组，里面第二个才是颜色的代码
#     root.config(bg=s1[1])
#
# Button(root,text='选择背景色',command=test).pack()
# root.mainloop()

'''文件对话框'''
# from tkinter.filedialog import *
# root = Tk()
# root.geometry('500x500')
# def test():
#     f = askopenfilename(title= '上传文件',initialdir='f:/file',filetypes=[('图片文件','.png')])
#     show['text'] = f
# Button(root,text="选择编辑的视频文件",command=test).pack()
# show = Label(root,width=40,height=3,bg="green")
# show.pack()
#
# root.mainloop()

'''子菜单的创建'''
# from tkinter.filedialog import *
#
#
# class Application(Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.master = master
#         self.textpad = None  # textpad 表示Text 文本框对象
#         self.pack()
#         self.createWidget()
#
#     def createWidget(self):
#         # 主菜单
#         menubar = Menu(root)
#         # 创建子菜单并添加为文件，添加到主菜单中。
#         file_menu = Menu(menubar)
#         menubar.add_cascade(label='文件', menu=file_menu)
#         # 给子菜单添加选项，用command关联函数
#         file_menu.add_command(label='打开', accelerator='open')
#         # 添加分割线
#         file_menu.add_separator()
#         file_menu.add_command(label='退出', accelerator="ctrl+q", command=self.test)
#
#         # 将主菜单加到跟窗口中农
#         root['menu'] = menubar
#
#         # 添加文本编辑区
#         self.textpad = Text(root, width=50, height=30)
#         self.textpad.pack()
#
#     def test(self):
#         pass
#
#
# if __name__ == '__main__':
#     root = Tk()
#     root.geometry('500x500')
#     root.title('简易记事本')
#     app = Application(master=root)
#     root.mainloop()
