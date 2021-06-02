from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

import player_manage
import round_manage
from win.record_win import Record_Manage


class Round_Manage(object):
    def __init__(self,match_id):
        """主界面基本设置"""
        # 创建窗口
        root = Toplevel()
        # 设置窗口大小和并将位置设置到屏幕中央
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        width = 700
        high = 600
        root.geometry('%dx%d+%d+%d' % (width, high, (screenwidth - width) / 2, (screenheight - high) / 2))

        #root.title(textvariable="123")

        # 设置各个文本框的标签，并固定位置
        Label(root, text="小局编号：").place(relx=0.54, rely=0.2, relwidth=0.1)
        Label(root, text="小局名称：").place(relx=0.54, rely=0.25, relwidth=0.1)
        Label(root, text="小局时间：").place(relx=0.54, rely=0.3, relwidth=0.1)
        #Label(root, text="比赛类型：").place(relx=0.54, rely=0.35, relwidth=0.1)
        # 设置各个文本框内容所对应的变量
        self.round_id = StringVar()
        self.round_name = StringVar()
        self.start_time = StringVar()

        # 设置各个文本框并固定位置
        Label(root, textvariable=self.round_id).place(relx=0.64, rely=0.2, relwidth=0.25, height=25)
        Entry(root, textvariable=self.round_name).place(relx=0.64, rely=0.25, relwidth=0.25, height=25)
        Entry(root, textvariable=self.start_time).place(relx=0.64, rely=0.3, relwidth=0.25, height=25)

        # 设置窗口的标题标签
        Label(root, text='小局信息管理', bg='white', fg='red', font=('宋体', 15)).pack(side=TOP, fill='x')

        # 创建表格并设置相关属性
        self.tree_view = ttk.Treeview(root, show='headings', column=('round_name','start_time'))
        sb = Scrollbar(root, orient='vertical', command=self.tree_view.yview)
        sb.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
        # 设置每列的属性
        self.tree_view.configure(yscrollcommand=sb.set)
        self.tree_view.column('round_name', width=120, anchor="center")
        self.tree_view.column('start_time', width=120, anchor="center")
        # 设置表格位置

        # 设置每行的属性
        self.tree_view.heading('round_name', text='大场比赛编号', command=lambda: player_manage.TreeviewSortColumn().table_sort(self.tree_view, 'round_name', False))
        self.tree_view.heading('start_time', text='比赛名称', command=lambda: player_manage.TreeviewSortColumn().table_sort(self.tree_view, 'start_time', False))

        self.tree_view.place(relx=0.02, rely=0.2, relwidth=0.5,relheight=0.6)

        round_manage.ShowRoundInfo(self.tree_view, match_id)
        # 设置按钮，并固定位置
        Button(root, text="添加", command=lambda: self.Add(match_id)).place(relx=0.1, rely=0.81, width=50)
        Button(root, text="删除", command=lambda: self.Del(match_id)).place(relx=0.2, rely=0.81, width=50)
        Button(root, text="修改", command=lambda: self.Modify(match_id)).place(relx=0.30, rely=0.81, width=50)
        Button(root, command=lambda: self.EnterRound(),text="进入小局").place(relx=0.64, rely=0.5, relwidth=0.25, height=25)
        Button(root, text="返回", command=lambda:self.callback(root)).place(relx=0.9, rely=0.01, width=50)
        self.tree_view.heading('round_name', text='小局比赛名称')
        self.tree_view.heading('start_time', text='小局比赛时间')
        # 创建一个顶级菜单
        menubar = Menu(root)

        # 创建下拉菜单，然后将它添加到顶级菜单中
        filemenu = Menu(menubar, tearoff=False)

        # 设置下拉菜单的label
        menubar.add_cascade(label="选项", menu=filemenu)
        filemenu.add_separator()
        filemenu.add_command(label="退出", command=lambda: self.callback(root))


        # 显示菜单
        root.config(menu=menubar)

        # 绑定单击离开事件
        self.tree_view.bind('<ButtonRelease-1>', self.tree_view_click)

        # 捕获关闭按钮
        root.protocol("WM_DELETE_WINDOW", lambda: self.callback(root))

        # 事件循环
        root.mainloop()

    def tree_view_click(self, event):
        """点击表格中的一项数据后将其显示在相应文本框上"""
        for item in self.tree_view.selection():
            item_text = self.tree_view.item(item, "values")
            #rint(item_text)
            self.round_id.set(item_text[2])
            self.round_name.set(item_text[0])
            self.start_time.set(item_text[1])

    def callback(self, root):
        """退出时的询问"""
        root.destroy()
    def EnterRound(self):
        if (not (self.round_id.get().strip())):
            showerror("错误", "请点击需要进入的比赛")
            return
        Record_Manage(self.round_id.get())


    def Add(self,match_id):
        round_manage.AddRoundInfo(self.tree_view, match_id, self.round_name, self.start_time)
        self.Clear_Info()
    def Del(self,match_id):
        round_manage.DelRoundInfo(self.tree_view, match_id, self.round_id, self.round_name, self.start_time)
        self.Clear_Info()
    def Modify(self,match_id):
        round_manage.ModifyRoundInfo(self.tree_view, match_id, self.round_id, self.round_name, self.start_time)
        self.Clear_Info()
    def Clear_Info(self):
        self.round_id.set('')
        self.round_name.set('')
        self.start_time.set('')