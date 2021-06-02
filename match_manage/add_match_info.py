from database import Database
from tkinter.messagebox import *
from .show_match_info import *

class AddMatchInfo(object):
    def __init__(self,tree_view, match_name,start_time,type,playerA_id,playerC_id):
        """添加比赛信息"""
        db = Database()
        if(not(match_name.get().strip())):
            showerror("添加失败", "比赛名称为空")
            return
        if(not(type.get().strip())):
            showerror("添加失败", "比赛类型为空")
            return
        match_name=match_name.get()
        start_time = start_time.get()
        playerA_id=playerA_id.get()
        playerC_id=playerC_id.get()
        type = type.get()

        print(match_name)
        print(start_time)
        print(type)
        try:
            if db.prepare(f"select * from match_table where match_name='{match_name}'") == 0:
                sql=(f"insert into match_table (match_name,start_time,type,playerA_id,playerC_id) values ('{match_name}','{start_time}',{type},{playerA_id},{playerC_id})")
                db.prepare(sql)
                db.update()
                showinfo("提示", "添加成功")
                ShowMatchInfo(tree_view)
            else:
                showerror("添加失败", "该比赛名称重复")
        except ValueError:
            showerror("添加失败", "信息未填写完整或有错误")

