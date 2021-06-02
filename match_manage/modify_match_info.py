from database import Database
from tkinter.messagebox import *
from .show_match_info import ShowMatchInfo

class ModifyMatchInfo(object):
    def __init__(self, tree_view,match_id,match_name,start_time,match_type,playerA_id,playerC_id):
        """修改学生信息"""
        db = Database()
        id_str = str(match_id.get())
        name = match_name.get()
        playerA_id=playerA_id.get()
        playerC_id=playerC_id.get()
        #print(id)
        try:
            if not (id_str.strip() and name.strip()):
                raise ValueError
            id= int(id_str)
            start_time = start_time.get()
            match_type=match_type.get()
            #print(type(match_type))
            if db.prepare(f"select * from match_table where match_id={id}") != 0:
                db.prepare(f"update match_table set match_id={id},match_name='{name}', start_time='{start_time}',"
                           f"type={match_type},playerA_id={playerA_id},playerC_id={playerC_id} where match_id={id}")
                db.update()
                showinfo("提示", "修改成功")
                ShowMatchInfo(tree_view)
            else:
                showerror("修改失败", "未查询到该参赛选手信息")
        except ValueError:
            showerror("修改失败", "信息未填写完整或者输入不合法")
        db.close()
