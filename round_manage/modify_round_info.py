from database import Database
from tkinter.messagebox import *
from .show_round_info import ShowRoundInfo

class ModifyRoundInfo(object):
    def __init__(self, tree_view,match_id,round_id,round_name,start_time):
        """修改学生信息"""
        db = Database()
        round_id = round_id.get()
        round_name = round_name.get()
        start_time=start_time.get()
        #print(id)
        try:
            if not (round_id.strip() and round_name.strip()):
                raise ValueError
            if db.prepare(f"select * from round_table where round_id={round_id}") != 0:
                db.prepare(f"update round_table set round_id={round_id},round_name='{round_name}', start_time='{start_time}'"
                           f"where round_id={round_id}")
                db.update()
                showinfo("提示", "修改成功")
                ShowRoundInfo(tree_view,match_id)
            else:
                showerror("修改失败", "未查询到该小轮手信息")
        except ValueError:
            showerror("修改失败", "信息未填写完整或者输入不合法")
        db.close()
