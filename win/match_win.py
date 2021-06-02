from tkinter import ttk
import match_manage
from player_manage.sort_player import TreeviewSortColumn
from .select_player_win import Select_Player
from .round_win import *
import player_manage
import tkinter as tk

class Match_Manage(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        width = 700
        high = 600
        self.geometry('%dx%d+%d+%d' % (width, high, (screenwidth - width) / 2, (screenheight - high) / 2))

        self.title('大局比赛管理系统')

        # 设置各个文本框的标签，并固定位置
        Label(self, text="比赛编号：").place(relx=0.54, rely=0.2, relwidth=0.1)
        Label(self, text="比赛名称：").place(relx=0.54, rely=0.25, relwidth=0.1)
        Label(self, text="比赛时间：").place(relx=0.54, rely=0.3, relwidth=0.1)
        Label(self, text="比赛类型：").place(relx=0.54, rely=0.35, relwidth=0.1)

        Label(self, text="对战双方：").place(relx=0.54, rely=0.4, relwidth=0.1)
        Button(self, command=lambda: self.SelectA(), text="选择选手A").place(relx=0.64, rely=0.45, relwidth=0.1)
        Button(self, command=lambda: self.SelectC(), text="选择选手C").place(relx=0.74, rely=0.45, relwidth=0.1)
        # 设置各个文本框内容所对应的变量
        self.match_id = StringVar()
        self.match_name = StringVar()
        self.start_time = StringVar()
        self.type = StringVar()

        self.playerA_id = StringVar()
        self.playerC_id = StringVar()
        # 设置各个文本框并固定位置
        Label(self, textvariable=self.match_id, justify=LEFT).place(relx=0.64, rely=0.2, relwidth=0.25, height=25)
        # Label(root, textvariable=self.match_id,justify='left').place(relx=0.64, rely=0.2, relwidth=0.25, height=25)
        Entry(self, textvariable=self.match_name).place(relx=0.64, rely=0.25, relwidth=0.25, height=25)
        Entry(self, textvariable=self.start_time).place(relx=0.64, rely=0.3, relwidth=0.25, height=25)
        Entry(self, textvariable=self.type).place(relx=0.64, rely=0.35, relwidth=0.25, height=25)

        Entry(self, textvariable=self.playerA_id).place(relx=0.64, rely=0.4, relwidth=0.1, height=25)
        Entry(self, textvariable=self.playerC_id).place(relx=0.74, rely=0.4, relwidth=0.1, height=25)

        # 设置窗口的标题标签
        Label(self, text='大局信息管理', bg='white', fg='red', font=('宋体', 15)).pack(side=TOP, fill='x')

        # 创建表格并设置相关属性
        self.tree_view = ttk.Treeview(self, show='headings', column=('match_id', 'match_name'))
        sb = Scrollbar(self, orient='vertical', command=self.tree_view.yview)
        sb.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
        # 设置每列的属性
        self.tree_view.configure(yscrollcommand=sb.set)
        self.tree_view.column('match_id', width=120, anchor="center")
        self.tree_view.column('match_name', width=120, anchor="center")
        # 设置每行的属性
        self.tree_view.heading('match_id', text='大场比赛编号',
                               command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'match_id', False))
        self.tree_view.heading('match_name', text='比赛名称',
                               command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'match_name', False))
        # 设置表格位置
        self.tree_view.place(relx=0.02, rely=0.2, relwidth=0.5, relheight=0.6)

        match_manage.ShowMatchInfo(self.tree_view)
        # 设置按钮，并固定位置
        Button(self, text="添加",
               command=lambda: self.Add()).place(relx=0.1, rely=0.81, width=50)
        Button(self, text="删除", command=lambda: self.Del()).place(
            relx=0.2, rely=0.81, width=50)
        Button(self, text="修改",
               command=lambda: self.Modify()).place(relx=0.30, rely=0.81,
                                                                                               width=50)
        Button(self, command=lambda: self.EnterMatch(), text="进入比赛").place(relx=0.64, rely=0.5, relwidth=0.25,
                                                                           height=25)
        Button(self, text="返回", command=lambda:self.callback()).place(relx=0.9, rely=0.01, width=50)
        # 创建一个顶级菜单
        menubar = Menu(self)

        # 创建下拉菜单，然后将它添加到顶级菜单中
        filemenu = Menu(menubar, tearoff=False)

        # 设置下拉菜单的label
        menubar.add_cascade(label="选项", menu=filemenu)
        filemenu.add_separator()
        filemenu.add_command(label="退出", command=lambda: self.callback())

        # 显示菜单
        self.config(menu=menubar)

        # 绑定单击离开事件
        self.tree_view.bind('<ButtonRelease-1>', self.tree_view_click)

        # 捕获关闭按钮
        self.protocol("WM_DELETE_WINDOW", lambda: self.callback())

    def tree_view_click(self, event):
        """点击表格中的一项数据后将其显示在相应文本框上"""
        for item in self.tree_view.selection():
            item_text = self.tree_view.item(item, "values")
            self.match_id.set(item_text[0])
            self.match_name.set(item_text[1])
            self.start_time.set(item_text[2])
            self.type.set(item_text[3])
            self.playerA_id.set(item_text[4])
            self.playerC_id.set(item_text[5])

    def callback(self):
        """退出时的询问"""
        self.destroy()

    def EnterMatch(self):
        if (not (self.match_id.get().strip())):
            showerror("错误", "请点击需要进入的比赛")
            return
        Round_Manage(self.match_id.get())

    def SelectA(self):
        inputDialog = Select_Player()
        self.wait_window(inputDialog)  # 这一句很重要！！！
        if(inputDialog.selectPlayer!=-1):
            print(inputDialog.selectPlayer)
            self.playerA_id.set(inputDialog.selectPlayer)

    def SelectC(self):
        inputDialog = Select_Player()
        self.wait_window(inputDialog)  # 这一句很重要！！！
        if(inputDialog.selectPlayer!=-1):
            print(inputDialog.selectPlayer)
            self.playerC_id.set(inputDialog.selectPlayer)

    def Add(self):
        match_manage.AddMatchInfo(self.tree_view, self.match_name, self.start_time,
                                  self.type, self.playerA_id, self.playerC_id)
        self.Clear_Info()
    def Del(self):
        match_manage.DelMatchInfo(self.tree_view, self.match_id)
        self.Clear_Info()
    def Modify(self):
        match_manage.ModifyMatchInfo(self.tree_view, self.match_id, self.match_name,
                                     self.start_time, self.type, self.playerA_id, self.playerC_id)
        self.Clear_Info()
    def Clear_Info(self):
        self.match_id.set('')
        self.match_name.set('')
        self.start_time.set('')
        self.type.set('')
        self.playerA_id.set('')
        self.playerC_id.set('')