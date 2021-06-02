from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *
from database import Database

import numpy as np
import matplotlib.pyplot as plt


class StatisticsInfo(object):
    def __init__(self):
        """创建显示统计的窗口"""

        top = Toplevel()
        self.db = Database()
        screenwidth = top.winfo_screenwidth()
        screenheight = top.winfo_screenheight()
        width = 700
        high = 600
        top.geometry('%dx%d+%d+%d' % (width, high, (screenwidth - width) / 2, (screenheight - high) / 2))

        # 创建显示数据的表格
        self.tree_view = ttk.Treeview(top, show='headings', column=('object', 'max', 'min', 'average', 'fail',
                                                                    'pass', 'middle', 'good', 'super', 'count'))
        self.tree_view.column('object', width=50, anchor="center")
        self.tree_view.column('max', width=50, anchor="center")
        self.tree_view.column('min', width=50, anchor="center")
        self.tree_view.column('average', width=50, anchor="center")
        self.tree_view.column('fail', width=50, anchor="center")
        self.tree_view.column('pass', width=50, anchor="center")
        self.tree_view.column('middle', width=50, anchor="center")
        self.tree_view.column('good', width=50, anchor="center")
        self.tree_view.column('super', width=50, anchor="center")
        self.tree_view.column('count', width=50, anchor="center")
        self.tree_view.heading('object', text='身体属性')
        self.tree_view.heading('max', text='最高')
        self.tree_view.heading('min', text='最低')
        self.tree_view.heading('average', text='平均')
        self.tree_view.heading('fail', text='<=20')
        self.tree_view.heading('pass', text='20< <=25')
        self.tree_view.heading('middle', text='25< <=30')
        self.tree_view.heading('good', text='30< <=35')
        self.tree_view.heading('super', text='>35')
        self.tree_view.heading('count', text='总人数')

        self.tree_view.place(relx=0.02, rely=0.3, relwidth=0.96)
        self.statistics()

    def statistics(self):
        """"统计数据并显示在表格上"""
        if self.db.prepare(
                "select max(age), min(age), round(avg(age),1), count(age<=20 or null), count(age<=25 and "
                "age>20 or null), count(25<age and age<=30 or null), count(30<age and age<=35 or "
                "null), count(35<age or null), count(*) from player") != 0:
            player_tuple = self.db.cursor.fetchall()
            player_tuple = ("年龄",) + player_tuple[0]
            #print(player_tuple)
            self.tree_view.insert("", 0, values=player_tuple)
            self.chart()
        else:
            showerror("统计失败", "没有运动员数据无法进行统计")

    def chart(self):
        """"统计数据的柱状图"""
        # 柱状图
        # 使图形中的中文正常编码显示
        #mpl.rcParams["font.sans-serif"] = ["SimHei"]
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
        # 每个柱子下标的索引
        self.db.prepare("select * from player")
        player_tuple = self.db.cursor.fetchall()
        index = self.db.cursor.description

        row = {}
        for i in range(len(index)):
            row[index[i][0]] = i
        self.db.close()
        x = np.arange(len(player_tuple))
        #print(x)

        y = [x[row['age']] for x in player_tuple]
        # 柱子的宽度
        bar_width = 0.35
        tick_label = [x[row['player_name']] for x in player_tuple]

        # 绘制柱状图并设置其各项属性
        plt.bar(x, y, bar_width, align="center", color="c", label="年龄", alpha=0.5)

        plt.tight_layout(pad=0.4, w_pad=10.0, h_pad=3.0)
        plt.title('运动员年龄统计表')
        plt.xlabel("姓名")
        plt.ylabel("年龄")

        plt.xticks(x + bar_width / 2, tick_label)
        plt.xticks(rotation=-90)
        plt.yticks(np.arange(0, 101, 20))

        # 添加图例
        plt.legend(loc="upper left")

        plt.show()
