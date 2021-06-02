from tkinter.messagebox import *
from database import Database


class TreeviewSortColumn(object):  # Treeview、列名、排列方式
    def table_sort(self, tv, col, reverse):
        """点击表头进行排序"""
        # 因为排序utf-8编号问题所以汉字排序不是按首字母来的所以转化为gbk编码
        if col == 'player_id' or col == 'player_age':
            l = [(int(tv.set(k, col)), k) for k in tv.get_children('')]
        else:
            l = [(tv.set(k, col), k) for k in tv.get_children('')]

        if col == 'player_name' or col=='player_sex' or col=='player_nationality':
            l = [(i[0].encode('GBK'), i[1]) for i in l]
            l.sort(reverse=reverse)
            l = [(i[0].decode('GBK'), i[1])for i in l]
        else:
            l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        col_dict = {True:'降序',False:'升序','player_id':'选手编号','player_name':'姓名','player_sex':'性别','player_age':'年龄','player_nationality':'国籍'}
        #showinfo("提示", f"已按{col_dict[col]}{col_dict[reverse]}排序")
        tv.heading(col, command=lambda: TreeviewSortColumn().table_sort(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题
