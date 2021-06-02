from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *


class Record_Manage(object):
    def __init__(self, match_id):
        """主界面基本设置"""
        # 创建窗口
        root = Toplevel()
        # 设置窗口大小和并将位置设置到屏幕中央
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        width = 700
        high = 600
        root.geometry('%dx%d+%d+%d' % (width, high, (screenwidth - width) / 2, (screenheight - high) / 2))

        # root.title(textvariable="123")

        # 设置各个文本框的标签，并固定位置
        # 设置各个文本框的标签，并固定位置
        Button(root, text="打开相机",command=lambda: self.OpenCamera()).place(relx=0.1, rely=0.2, relwidth=0.15)
        Button(root, text="开始录制",command=lambda: self.StartRecord()).place(relx=0.25, rely=0.2, relwidth=0.15)
        Button(root, text="停止录制",command=lambda: self.StopRecord()).place(relx=0.4, rely=0.2, relwidth=0.15)
        Button(root, text="关闭相机",command=lambda: self.CloseCamera()).place(relx=0.55, rely=0.2, relwidth=0.15)
        Button(root, text="本小局结束",command=lambda: self.CallBack(root)).place(relx=0.7, rely=0.2, relwidth=0.15)
        # Label(root, text="比赛类型：").place(relx=0.54, rely=0.35, relwidth=0.1)

        # 设置窗口的标题标签
        Label(root, text='比赛数据录制', bg='white', fg='red', font=('宋体', 15)).pack(side=TOP, fill='x')

        Button(root, text="返回", command=lambda:self.callback(root)).place(relx=0.9, rely=0.01, width=50)

        # 创建一个顶级菜单
        menubar = Menu(root)

        # 创建下拉菜单，然后将它添加到顶级菜单中
        filemenu = Menu(menubar, tearoff=False)

        # 设置下拉菜单的label
        menubar.add_cascade(label="选项", menu=filemenu)
        filemenu.add_separator()
        filemenu.add_command(label="退出", command=lambda: self.CallBack(root))

        # 显示菜单
        root.config(menu=menubar)


        # 捕获关闭按钮
        root.protocol("WM_DELETE_WINDOW", lambda: self.CallBack(root))
        
        # 事件循环
        root.mainloop()

    def OpenCamera(self):
        showinfo("提示", "已打开相机")
    def StartRecord(self):
        showinfo("提示", "已开始录制")
    def StopRecord(self):
        showinfo("提示", "已停止录制")
    def CloseCamera(self):
        showinfo("提示", "已关闭相机")
    def callback(self, root):
        """退出时的询问"""
        root.destroy()


