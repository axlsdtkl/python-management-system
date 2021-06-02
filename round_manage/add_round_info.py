from database import Database
from tkinter.messagebox import *
from .show_round_info import ShowRoundInfo


class AddRoundInfo(object):
    def __init__(self,tree_view,match_id,round_name,start_time):
        """添加学生信息"""
        db = Database()
        if(not(round_name.get().strip())):
            showerror("添加失败", "比赛名称为空")
            return
        round_name=round_name.get()
        start_time = start_time.get()
        try:
            if db.prepare(f"select * from round_table where round_name='{round_name}'and match_id={match_id}") == 0:
                sql=(f"insert into round_table (match_id,round_name,start_time) values ({match_id},'{round_name}','{start_time}')")
                db.prepare(sql)
                db.update()
                showinfo("提示", "添加成功")
                ShowRoundInfo(tree_view,match_id)
            else:
                showerror("添加失败", "该比赛名称重复")
        except ValueError:
            showerror("添加失败", "信息未填写完整或有错误")

