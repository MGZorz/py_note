'''
开发一个简单的记事本软件
功能：
    1、 新建文本文件
    2、 保存文件
    3、 修改文件内容
    4、 退出
    5、 各种快捷键处理
    6、 修改文本区域背景色
version1.0
'''
from tkinter.filedialog import *
from tkinter.colorchooser import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.textpad = None

        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建主菜单
        menubar = Menu(root)
        # 创建子菜单（文件+编辑+帮助）
        file_menu = Menu(menubar)
        edit_menu = Menu(menubar)
        help_menu = Menu(menubar)
        # 将子菜单添加到主菜单栏中
        menubar.add_cascade(label='文件', menu=file_menu)
        menubar.add_cascade(label='编辑', menu=edit_menu)
        menubar.add_cascade(label='帮助', menu=help_menu)
        # 在给每个子菜单添加菜单项
        file_menu.add_command(label='新建', accelerator='ctrl+n', command=self.newfile)
        file_menu.add_command(label='打开', accelerator='ctrl+o', command=self.openfile)
        file_menu.add_command(label='保存', accelerator='ctrl+s', command=self.savefile)
        # 添加个分界线
        file_menu.add_separator()
        file_menu.add_command(label='退出', accelerator='ctrl+q', command=self.exit)

        # 将菜单添加到主页面中
        root['menu'] = menubar

        # 快捷键处理
        root.bind('<Control-n>', lambda event: self.newfile())
        root.bind('<Control-o>', lambda event: self.oepnfile())
        root.bind('<Control-s>', lambda event: self.savefile())
        root.bind('<Control-q>', lambda event: self.exit())

        # 文本编辑区
        self.textpad = Text(root, width=50, height=50)
        self.textpad.pack()

        # 创建上下文菜单
        self.contextMenu = Menu(root)
        self.contextMenu.add_command(label='背景颜色', command=self.openAskColor)

        # 给右键绑定该事件
        root.bind('<Button-3>', self.createContextMenu)

    '''新建一个文件'''
    def newfile(self):
        self.textpad.delete('1.0', 'end')  # 把原来的Text中的内容清空
        self.filename = asksaveasfilename(title='另存为', initialfile='未命名.txt', filetypes=[('文本文件', '*.txt')],
                                          defaultextension='.txt')
        print(self.filename)
        self.savefile()

    '''打开一个文件'''
    def openfile(self):
        self.textpad.delete('1.0', 'end')  # 同样清空TExt
        with askopenfile(title='打开文件')as f:
            self.textpad.insert(INSERT, f.read())
            self.filename = f.name
            print(f.name)

    '''保存一个文件'''
    def savefile(self):
        with open(self.filename, 'w')as f:
            c = self.textpad.get('1.0', END)
            f.write(c)

    '''关闭'''
    def exit(self):
        root.quit()

    '''切换背景色'''
    def openAskColor(self):
        s1 = askcolor(color='red', title='选择背景色')
        self.textpad.config(bg=s1[1])

    '''菜单在右键点击的坐标上显示'''
    def createContextMenu(self, event):
        # 菜单在右键点击的坐标上显示
        self.contextMenu.post(event.x_root, event.y_root)


if __name__ == '__main__':
    root = Tk()
    root.geometry('500x500')
    root.title('简易记事本')
    app = Application(master=root)
    root.mainloop()
