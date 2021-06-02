from tkinter import *
from tkinter import ttk

from player_manage.sort_player import TreeviewSortColumn
import player_manage

import tkinter as tk
'''松耦合'''
# 弹窗

class Select_Player(tk.Toplevel):
    def __init__(self):
        super().__init__()
        """主界面基本设置"""
        # 设置窗口大小和并将位置设置到屏幕中央
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        width = 700
        high = 600
        self.geometry('%dx%d+%d+%d' % (width, high, (screenwidth - width) / 2, (screenheight - high) / 2))

        self.title('选手信息管理系统')

        # 设置各个文本框的标签，并固定位置
        Label(self, text="选手ID：").place(relx=0, rely=0.05, relwidth=0.1)
        Label(self, text="姓名：").place(relx=0, rely=0.1, relwidth=0.1)
        Label(self, text="性别：").place(relx=0.5, rely=0.1, relwidth=0.1)
        Label(self, text="年龄：").place(relx=0, rely=0.15, relwidth=0.1)
        Label(self, text="国籍：").place(relx=0.5, rely=0.15, relwidth=0.1)

        # 设置各个文本框内容所对应的变量
        self.player_id=StringVar()
        self.player_name = StringVar()
        self.player_sex = StringVar()
        self.player_age = StringVar()
        self.player_nationality = StringVar()

        # 设置各个文本框并固定位置
        Entry(self, textvariable=self.player_id).place(relx=0.1, rely=0.05, relwidth=0.35, height=25)
        Entry(self, textvariable=self.player_name).place(relx=0.1, rely=0.1, relwidth=0.35, height=25)
        Entry(self, textvariable=self.player_sex).place(relx=0.6, rely=0.1, relwidth=0.35, height=25)
        Entry(self, textvariable=self.player_age).place(relx=0.1, rely=0.15, relwidth=0.35, height=25)
        Entry(self, textvariable=self.player_nationality).place(relx=0.6, rely=0.15, relwidth=0.35, height=25)

        # 设置窗口的标题标签
        Label(self, text='选手信息管理', bg='white', fg='red', font=('宋体', 15)).pack(side=TOP, fill='x')

        # 创建表格并设置相关属性
        self.tree_view = ttk.Treeview(self, show='headings', column=('player_id','player_name', 'player_sex', 'player_age', 'player_nationality'))
        sb = Scrollbar(self, orient='vertical', command=self.tree_view.yview)
        sb.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
        # 设置每列的属性
        self.tree_view.configure(yscrollcommand=sb.set)
        self.tree_view.column('player_id', width=120, anchor="center")
        self.tree_view.column('player_name', width=120, anchor="center")
        self.tree_view.column('player_sex', width=120, anchor="center")
        self.tree_view.column('player_age', width=120, anchor="center")
        self.tree_view.column('player_nationality', width=120, anchor="center")
        # 设置每行的属性
        self.tree_view.heading('player_id', text='选手id', command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'player_id', False))
        self.tree_view.heading('player_name', text='姓名', command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'player_name', False))
        self.tree_view.heading('player_sex', text='性别', command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'player_sex', False))
        self.tree_view.heading('player_age', text='年龄', command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'player_age', False))
        self.tree_view.heading('player_nationality', text='国籍', command=lambda: TreeviewSortColumn().table_sort(self.tree_view, 'player_nationality', False))
        # 设置表格位置
        self.tree_view.place(relx=0.02, rely=0.3, relwidth=0.96)

        # 设置按钮，并固定位置
        player_manage.ShowPlayerInfo(self.tree_view)
        Button(self, text="显示所有信息", command=lambda: player_manage.ShowPlayerInfo(self.tree_view)).place(relx=0.05, rely=0.2, width=100)
        Button(self, text="添加运动员信息", command=lambda: player_manage.AddPlayerInfo(self.tree_view,self.player_id, self.player_name, self.player_sex, self.player_age, self.player_nationality)).place(relx=0.20, rely=0.2, width=100)
        Button(self, text="删除运动员信息", command=lambda: player_manage.DelPlayerInfo(self.tree_view,self.player_id, self.player_name, self.player_sex, self.player_age, self.player_nationality)).place(relx=0.35, rely=0.2, width=100)
        Button(self, text="修改运动员信息", command=lambda: player_manage.ModifyPlayerInfo(self.tree_view,self.player_id,self.player_name, self.player_sex, self.player_age, self.player_nationality)).place(relx=0.50, rely=0.2, width=100)
        Button(self, text="统计运动员信息", command=lambda: player_manage.StatisticsInfo()).place(relx=0.65, rely=0.2, width=100)
        Button(self, text="查询运动员信息", command=lambda: player_manage.SearchPlayerInfo(self.player_id,self.player_name, self.player_sex, self.player_age, self.player_nationality, self.tree_view)).place(relx=0.80, rely=0.2, width=100)

        Button(self, text="选择运动员", command=lambda: self.select_ID()).place(relx=0.45, rely=0.7, width=100)
        Button(self, text="返回", command=lambda:self.callback(self)).place(relx=0.9, rely=0.01, width=50)
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
            self.player_id.set(item_text[0])
            self.player_name.set(item_text[1])
            self.player_sex.set(item_text[2])
            self.player_age.set(item_text[3])
            self.player_nationality.set(item_text[4])

    def callback(self):
        """退出时的询问"""
        self.selectPlayer=-1
        self.destroy()

    def select_ID(self):
        self.selectPlayer = self.player_id.get()  # 设置数据
        self.destroy()  # 销毁窗口


