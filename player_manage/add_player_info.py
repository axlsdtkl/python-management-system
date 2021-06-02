from database import Database
from tkinter.messagebox import *
from .show_player_info import ShowPlayerInfo


class AddPlayerInfo(object):
    def __init__(self,tree_view, player_id,player_name, player_sex, player_age, player_nationality):
        """添加学生信息"""
        db = Database()
        if(not(player_id.get().strip())):
            showerror("添加失败", "选手编号为空")
            return
        id=int(player_id.get())
        name = player_name.get()
        sex = player_sex.get()
        try:
            if not(name.strip()):
                raise ValueError
            if (not (player_id.get().strip())):
                age = int(player_age.get())
            else:
                age=0;
            nationality = str(player_nationality.get())

            if db.prepare(f"select * from player where player_id='{id}'") == 0:
                sql=(f"insert into player (player_id,player_name,sex,age,nationality) values ({id},'{name}','{sex}',{age},'{nationality}')")
                db.prepare(sql)
                db.update()
                showinfo("提示", "添加成功")
                ShowPlayerInfo(tree_view)
            else:
                showerror("添加失败", "该ID重复")
        except ValueError:
            showerror("添加失败", "信息未填写完整或有错误")

